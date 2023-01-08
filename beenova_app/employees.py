from flask import Blueprint, redirect, render_template, session, url_for

from beenova_app.forms import RegisterEmployeeForm
from beenova_app.db_queries import DBOperator

bp = Blueprint('employees', __name__, url_prefix='/employees')


@bp.route('/register_employee', methods=('GET', 'POST'))
def register_employee():
    form = RegisterEmployeeForm()
    error = None
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        phone_number = form.phone_number.data
        is_company_admin = form.is_company_admin.data

        if not first_name or not last_name or not email or not phone_number:
            error = "Please fill all required fields."

        if error is None:
            db_operator = DBOperator()
            # register employee
            db_operator.create_employee(
                first_name=first_name,
                last_name=last_name,
                created_by=session.get('user_id') if 'user_id' in session else 0,
                username=email,
                email=email,
                company=None,
                phone_number=phone_number,
                is_admin=0,
                is_company_admin=is_company_admin,
                is_activated=0
            )

            return redirect(url_for("index"))
    return render_template('employees/register_employee.html', form=form, error=error)
