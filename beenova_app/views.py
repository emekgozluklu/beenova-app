from flask import render_template, redirect, url_for, session
from beenova_app.auth import logout_required
from beenova_app.forms import RequestDemoForm
from beenova_app.db_queries import DBOperator


def index():
    if session.get('user_id'):
        return redirect(url_for('app.company_dashboard'))
    return render_template("index.html")


@logout_required
def request_demo():
    form = RequestDemoForm()
    error = None
    db_operator = DBOperator()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        company = form.company.data
        phone_number = form.phone_number.data
        message = form.message.data

        if not first_name or not last_name or not email:
            error = "Please fill all required fields."
        if error is None:
            db_operator.create_request_demo(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                company=company,
                message=message
            )

            return redirect(url_for("index"))

    return render_template('request_demo.html', form=form, error=error)
