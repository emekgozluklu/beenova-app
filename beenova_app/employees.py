from flask import Blueprint, redirect, render_template, session, url_for
from werkzeug.security import generate_password_hash

from beenova_app.forms import RegisterEmployeeForm
from beenova_app.db_queries import DBOperator

bp = Blueprint('employees', __name__, url_prefix='/employees')


@bp.route('/register_employee', methods=('GET', 'POST'))
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
                company=None,
                phone_number=phone_number,
                is_admin=0,
                is_company_admin=is_company_admin,
                is_activated=0
            )

            return redirect(url_for("index"))
    return render_template('employees/register_employee.html', form=form, error=error)
