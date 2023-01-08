from flask import Blueprint, redirect, render_template, session, url_for
from werkzeug.security import generate_password_hash

from beenova_app.forms import RegisterCompanyForm
from beenova_app.db_queries import DBOperator


bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/register_company', methods=('GET', 'POST'))
def register_company():
    form = RegisterCompanyForm()
    error = None
    db_operator = DBOperator()
    if form.validate_on_submit():
        company_name = form.company_name.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        phone_number = form.phone_number.data
        password = form.password.data
        confirm = form.confirm.data

        c = db_operator.get_company_by_name(company_name)
        print("check")

        if not company_name or not first_name or not last_name or not email or not phone_number:
            error = "Please fill all required fields."
        elif c is not None:
            error = "Company with this name already exists."
        elif password != confirm:
            error = "Passwords do not match."

        if error is None:

            # register employee
            db_operator.create_employee(
                first_name=first_name,
                last_name=last_name,
                created_by=session.get('user_id') if 'user_id' in session else 0,
                username=email,
                email=email,
                password_hash=generate_password_hash(password),
                company=None,
                phone_number=phone_number,
                is_admin=0,
                is_company_admin=1,
                is_activated=0
            )

            company_admin_id = db_operator.get_employee_by_email(email)["id"]

            try:
                # register company
                db_operator.register_company(
                    name=company_name,
                    admin_id=company_admin_id,
                )

                # set company as employee's company
                company_id = db_operator.get_company_by_name(company_name)["id"]
                db_operator.update_employee_with_id(company_admin_id, company=company_id)

            except Exception as e:
                db_operator.delete_employee_by_id(company_admin_id)
                render_template('admin/register_company.html', form=form, error=e)

            return redirect(url_for("index"))

    return render_template('admin/register_company.html', form=form, error=error)
