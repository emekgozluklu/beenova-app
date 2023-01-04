from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()],
                        render_kw={'class': 'form-control'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'class': 'form-control'})
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In', render_kw={'class': 'form-group button-primary'})

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)


class RequestDemoForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=3, max=32)],
                             render_kw={'class': 'form-control'})
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=3, max=32)],
                            render_kw={'class': 'form-control'})
    email = StringField('Company Email', validators=[DataRequired(), Length(1, 64), Email()],
                        render_kw={'class': 'form-control'})
    message = StringField('Your Message', validators=[Length(1, 500)], render_kw={'class': 'form-control'})

    def __init__(self, *args, **kwargs):
        super(RequestDemoForm, self).__init__(*args, **kwargs)
