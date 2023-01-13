import os
from collections import defaultdict

from flask import Blueprint, redirect, render_template, session, url_for, current_app
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename

from beenova_app.forms import RegisterEmployeeForm, CreateDataSourceForm, RequestDataSourceForm
from beenova_app.db_queries import DBOperator
from beenova_app.auth import login_required
from beenova_app.utils import DataSourceFileHandler


bp = Blueprint('app', __name__, url_prefix='/app')


@bp.route('/company')
@login_required
def company_dashboard():
    db_operator = DBOperator()
    ds_table_rows = db_operator.get_data_sources_of_company_for_dashboard_table(session.get('user_company_id'))
    data = {
        'numbers': defaultdict(int),
        'table_rows': ds_table_rows,
        'data_usages': {
            'DS1': 5.2,
            'DS2': 4.9,
            'DS3': 9.1
        }
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


@bp.route('/request_data_source', methods=('GET', 'POST'))
@login_required
def request_data_source():
    form = RequestDataSourceForm()
    error = None
    db_operator = DBOperator()

    form.data_source.choices = db_operator.get_data_sources()
    
    if form.validate_on_submit():

        requester = session.get('user_id')
        data_source = form.data_source.data
        request_message = form.request_message.data

        if not requester or not data_source or not request_message:
            error = "Please fill all required fields."
        
        if error is None:
            # create request
            db_operator.create_request(requester=requester, data_source=data_source, 
                                       request_message=request_message)

            return redirect(url_for("index"))
    return render_template('app/request_data_source.html', form=form, error=error)


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
        file = form.file.data
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

            data_source_id = db_operator.get_data_source_id_by_file_save_path(file_save_path)
            ds_handler = DataSourceFileHandler(data_source_id, file_save_path)
            ds_handler.handle_csv()

            return redirect(url_for("app.company_dashboard"))
    return render_template('app/upload_data_source.html', form=form, error=error)

