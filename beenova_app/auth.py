import functools
from flask import Blueprint, g, redirect, render_template, session, url_for
from werkzeug.security import check_password_hash

from beenova_app.db_queries import DBOperator
from beenova_app.forms import RequestDemoForm, LoginForm

bp = Blueprint('auth', __name__, url_prefix='/auth')


def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = user_id


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if 'user_id' not in session:
            return redirect(url_for("index"))
        return view(**kwargs)
    return wrapped_view


def logout_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if 'user_id' in session:
            return redirect(url_for("index"))
        return view(**kwargs)
    return wrapped_view


@bp.route('/login', methods=('GET', 'POST'))
@logout_required
def login():
    form = LoginForm()
    error = None
    db_operator = DBOperator()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = db_operator.get_employee_by_email(email)

        if user is None:
            error = "User does not exist!"
        elif not check_password_hash(user['password_hash'], password):
            error = "Incorrect password!"

        if error is None:
            session.clear()
            session["user_id"] = user["id"]
            session["user_is_admin"] = user["is_admin"]
            session["user_is_company_admin"] = user["is_company_admin"]
            session["user_company_id"] = user["company"]

            if session["user_is_admin"]:
                return redirect(url_for("admin.register_company"))
                # return redirect(url_for("admin.index"))
            else:
                return redirect(url_for("app.company_dashboard"))
                # return redirect(url_for("employee.index"))

    return render_template("auth/login.html", form=form, error=error)


@bp.route('/logout')
@login_required
def logout():
    session.clear()
    return redirect(url_for("index"))
