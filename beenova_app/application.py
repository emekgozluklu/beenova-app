import os
from collections import defaultdict

from flask import Blueprint, redirect, render_template, session, url_for, current_app, request, jsonify
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename

from beenova_app.forms import RegisterEmployeeForm, CreateDataSourceForm, RequestDataSourceForm, AcceptRequestForm, RejectRequestForm
from beenova_app.db_queries import DBOperator
from beenova_app.auth import login_required
from beenova_app.utils import DataSourceFileHandler, APIRequestHandler, transform_marketplace_data, explain_status


bp = Blueprint('app', __name__, url_prefix='/app')


@bp.route('/marketplace')
@login_required
def marketplace():
    db_operator = DBOperator()
    data_sources = db_operator.get_available_data_sources(excluded_company_id=session['user_company_id'])
    data = transform_marketplace_data(data_sources)

    if len(data.keys()) == 0:
        return render_template('app/marketplace.html', data=None, no_data=True)

    return render_template('app/marketplace.html', data=data, no_data=False)


@bp.route('/data_source/<int:data_source_id>')
@login_required
def data_source_detail(data_source_id):
    db_operator = DBOperator()
    data_source_id = int(data_source_id)
    data_source = db_operator.get_data_source_by_id(data_source_id)
    data_source = dict(data_source) if data_source else None

    user_managed_data_sources = db_operator.get_user_managed_data_source_ids(session['user_id'])
    user_subscribed_data_sources = db_operator.get_user_subscribed_data_source_ids(session['user_company_id'])

    user_is_admin = data_source_id in user_managed_data_sources
    user_is_subscribed = data_source_id in user_subscribed_data_sources

    return render_template('app/data_source_detail.html',
                           data_source=data_source,
                           user_is_admin=user_is_admin,
                           user_is_subscribed=user_is_subscribed
                           )


@bp.route('/company')
@login_required
def company_dashboard():
    db_operator = DBOperator()

    numbers = db_operator.get_dashboard_numbers(session['user_company_id'])
    ds_table_rows = db_operator.get_data_sources_of_company_for_dashboard_table(session.get('user_company_id'))
    subscriptions = db_operator.get_subscriptions_of_company_for_dashboard_table(session.get('user_company_id'))
    data_usage_per_ds = db_operator.get_data_usages_of_company(session.get('user_company_id'))

    data = {
        'numbers': numbers,
        'data_sources': ds_table_rows,
        'subscriptions': subscriptions,
        'data_usages': data_usage_per_ds
    }
    return render_template('app/company_dashboard.html', data=data)


@bp.route('/register_employee', methods=('GET', 'POST'))
@login_required
def register_employee():
    form = RegisterEmployeeForm()
    error = None
    db_operator = DBOperator()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        phone_number = form.phone_number.data
        is_company_admin = form.is_company_admin.data
        password = form.password.data
        confirm = form.confirm.data

        u = db_operator.get_employee_by_email(email)

        if not first_name or not last_name or not email or not phone_number:
            error = "Please fill all required fields."
        elif u is not None:
            error = "User {} is already registered.".format(email)
        elif password != confirm:
            error = "Passwords do not match."

        if error is None:
            db_operator = DBOperator()
            # register employee
            db_operator.create_employee(
                first_name=first_name,
                last_name=last_name,
                created_by=session.get('user_id') if 'user_id' in session else 0,
                username=email,
                email=email,
                password_hash=generate_password_hash(password),
                company=session.get('user_company_id'),
                phone_number=phone_number,
                is_admin=0,
                is_company_admin=is_company_admin,
                is_activated=0
            )

            return redirect(url_for("index"))
    return render_template('app/register_employee.html', form=form, error=error)


@bp.route('/request/<data_source_id>', methods=('GET', 'POST'))
@login_required
def request_data_source(data_source_id):
    form = RequestDataSourceForm()
    error = None
    db_operator = DBOperator()
    data_source_id = int(data_source_id)

    available_data_sources = db_operator.get_available_data_sources()
    available_data_source_ids = [ds['id'] for ds in available_data_sources]

    requested_ds = defaultdict(str)

    if data_source_id not in available_data_source_ids:
        error = "Data source is not available!"
    else:
        requested_ds = dict(available_data_sources[available_data_source_ids.index(data_source_id)])

    if form.validate_on_submit():
        requester = session.get('user_id')
        request_message = form.request_message.data

        if not request_message:
            error = "Please fill all required fields."

        if error is None:
            # create request
            db_operator.create_request(requester=requester, data_source=data_source_id,
                                       request_message=request_message)

            return redirect(url_for("index"))
    return render_template('app/request_data_source.html', form=form, error=error, requested_ds=requested_ds)


@bp.route('/upload_data_source', methods=('GET', 'POST'))
@login_required
def upload_data_source():
    form = CreateDataSourceForm()
    error = None
    db_operator = DBOperator()

    form.data_source_type.choices = db_operator.get_data_source_types()
    form.responsible_employee.choices = db_operator.get_employees_of_company(session.get('user_company_id'))

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        publish = form.publish.data
        is_private = form.is_private.data
        data_source_type = form.data_source_type.data
        subscription_fee = form.subscription_fee.data
        responsible_employee = form.responsible_employee.data

        company_id = db_operator.get_employee_by_id(session.get('user_id'))['company']
        filename = secure_filename(form.file.data.filename)
        file_save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], str(company_id), filename)

        if not title or not description or not data_source_type or not responsible_employee:
            error = "Please fill all required fields."

        if error is None:
            os.makedirs(os.path.dirname(file_save_path), exist_ok=True)
            form.file.data.save(file_save_path)

            db_operator.create_data_source(
                title=title,
                description=description,
                is_published=publish,
                type_id=data_source_type,
                data_root=file_save_path,
                is_private=is_private,
                subscription_fee=subscription_fee,
                responsible_employee=responsible_employee,
                created_by=session.get('user_id')
            )
            data_source_id = db_operator.get_data_source_by_title(title)['id']
            db_operator.create_data_source_permission(data_source_id, responsible_employee, 'read')
            db_operator.create_data_source_permission(data_source_id, responsible_employee, 'write')
            db_operator.create_data_source_permission(data_source_id, responsible_employee, 'delete')

            data_source_id = db_operator.get_data_source_id_by_file_save_path(file_save_path)

            ds_handler = DataSourceFileHandler(data_source_id, file_save_path)
            ds_handler.handle_csv()

            return redirect(url_for("app.company_dashboard"))
    return render_template('app/upload_data_source.html', form=form, error=error)

@bp.route('/api/v1/<table_name>/<method>', methods=('GET',))
@login_required
def api_v1(table_name, method):
    # check is data source exists
    db_operator = DBOperator()
    data_source_exists = db_operator.check_if_data_source_exists(table_name)
    method_valid = method in ['read', 'write', 'delete']
    user_has_permission = db_operator.check_if_user_has_permission(table_name, session.get('user_id'), method)
    args = request.args.to_dict()
    if data_source_exists and method_valid:
        result = APIRequestHandler(args, table_name, method).handle_request()
        if type(result) is tuple:
            return result
        result = [tuple(row) for row in result]
        return jsonify(result)
    else:
        return jsonify({'error': 'Access denied'})

@bp.route('/user_account')
@login_required
def user_account():
    db_operator = DBOperator()
    user = db_operator.get_employee_by_id(session.get('user_id'))
    ds_table_rows = db_operator.get_data_sources_by_responsible_employee_id(session.get('user_id'))
    user_info = {
        'name': user['first_name'] + ' ' + user['last_name'],
        'profile_photo': url_for('static', filename='profile_pics/' + user['profile_photo']) ,
        'username': user['username'],
        'email': user['email'],
        'phone_number': user['phone_number'],
        'company': db_operator.get_company_by_id(user['company'])['name'],
        'table_rows': ds_table_rows
    }

    return render_template('app/user_account.html', user_info=user_info)

@bp.route('/pending_requests')
@login_required
def pending_requests():
    db_operator = DBOperator()
    requests_table_rows = db_operator.get_pending_requests_of_employee(session.get('user_id'))
    requests_table_rows = explain_status(requests_table_rows)
    return render_template('app/pending_requests.html', requests_table_rows=requests_table_rows)

@bp.route('/pending_requests/<request_id>', methods=('GET', 'POST'))
@login_required
def edit_request(request_id):
    db_operator = DBOperator()
    accept_form = AcceptRequestForm()
    reject_form = RejectRequestForm()
    user_info = db_operator.get_request_related_info_by_id(request_id)
    photo_url = url_for('static', filename='profile_pics/' + user_info['profile_photo'])
    # send query if accepted
    requester_id = user_info['id']
    data_source_id = user_info['data_source_id']
    
    if accept_form.validate_on_submit():
        db_operator.accept_request(request_id, requester_id, data_source_id)
        return redirect(url_for('app.pending_requests'))

    if reject_form.validate_on_submit():
        db_operator.reject_request(request_id)
        return redirect(url_for('app.pending_requests'))

    return render_template('app/edit_request.html', user_info=user_info, photo_url=photo_url, acceptRequestForm=accept_form, rejectRequestForm=reject_form)