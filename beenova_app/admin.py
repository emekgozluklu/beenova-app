from flask import Blueprint, redirect, render_template, session, url_for

from beenova_app.forms import RegisterCompanyForm
from beenova_app.db_queries import DBOperator

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/register_company', methods=('GET', 'POST'))
def register_company():
    form = RegisterCompanyForm()
    error = None
    if form.validate_on_submit():
        company_name = form.company_name.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        phone_number = form.phone_number.data

        if not company_name or not first_name or not last_name or not email or not phone_number:
            error = "Please fill all required fields."
        if error is None:
            db_operator = DBOperator()
            # register employee
            db_operator.register_employee(
                first_name,
                last_name,
                email,
                phone_number,
                is_company_admin=1,
                created_by=session.get('user_id') if 'user_id' in session else 0
            )

            company_admin_id = db_operator.get_employee_id_by_email(email)["id"]

            try:
                # register company
                db_operator.register_company(
                    name=company_name,
                    admin_id=company_admin_id,
                )
            except Exception as e:
                db_operator.delete_employee_by_id(company_admin_id)
                render_template('admin/register_company.html', form=form, error=error)

            return redirect(url_for("index"))

    return render_template('admin/register_company.html', form=form, error=error)
