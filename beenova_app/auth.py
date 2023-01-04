import functools
from flask import Blueprint, g, redirect, render_template, session, url_for
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


@bp.route('/request_demo', methods=('GET', 'POST'))
@logout_required
def request_demo():
    form = RequestDemoForm()
    error = None
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        message = form.message.data

        if not first_name or not last_name or not email:
            error = "Please fill all required fields."
        if error is None:
            # save request to the database
            return redirect(url_for("index"))

    return render_template('auth/request_demo.html', form=form, error=error)


@bp.route('/login', methods=('GET', 'POST'))
@logout_required
def login():
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = 1  # get user from database

        if user is None:
            error = "User does not exist!"

        # check if the password is correct

        if error is None:
            session.clear()
            session["user_id"] = 1
            # set user session variables

            return redirect(url_for("index"))
    return render_template("auth/login.html", form=form, error=error)


@bp.route('/logout')
@login_required
def logout():
    session.clear()
    return redirect(url_for("index"))
