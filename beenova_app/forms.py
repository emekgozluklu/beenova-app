from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, BooleanField, SubmitField, SelectField, FileField, TextAreaField, FloatField
)
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


class RegisterCompanyForm(FlaskForm):
    company_name = StringField('Company Name', validators=[DataRequired(), Length(min=3, max=32)],
                               render_kw={'class': 'form-control'})

    # responsible employee form
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=3, max=32)],
                             render_kw={'class': 'form-control'})
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=3, max=32)],
                            render_kw={'class': 'form-control'})
    email = StringField('Company Email', validators=[DataRequired(), Length(1, 64), Email()],
                        render_kw={'class': 'form-control'})

    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=3, max=32)],
                               render_kw={'class': 'form-control'})

    def __init__(self, *args, **kwargs):
        super(RegisterCompanyForm, self).__init__(*args, **kwargs)


class RegisterEmployeeForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=3, max=32)],
                             render_kw={'class': 'form-control'})
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=3, max=32)],
                            render_kw={'class': 'form-control'})
    email = StringField('Company Email', validators=[DataRequired(), Length(1, 64), Email()],
                        render_kw={'class': 'form-control'})
    phone_number = StringField('Phone Number', validators=[Length(min=3, max=32)],
                               render_kw={'class': 'form-control'})
    is_company_admin = BooleanField('Company Admin', render_kw={'class': 'form-control'})

    def __init__(self, *args, **kwargs):
        super(RegisterEmployeeForm, self).__init__(*args, **kwargs)


class CreateDataSourceForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=3, max=32)],
                        render_kw={'class': 'form-control'})

    description = TextAreaField('Description', validators=[DataRequired(), Length(min=3, max=500)],
                                render_kw={'class': 'form-control'})

    publish = BooleanField('Publish', render_kw={'class': 'form-control'})
    is_private = BooleanField('Private', render_kw={'class': 'form-control'})
    type = SelectField('Data Source Type', render_kw={'class': 'form-control'})
    file = FileField('Source File', render_kw={'class': 'form-control'})
    subscription_fee = FloatField('Subscription Fee', render_kw={'class': 'form-control'})
    responsible_employee = SelectField('Responsible Employee', render_kw={'class': 'form-control'})

    def __init__(self, *args, **kwargs):
        super(CreateDataSourceForm, self).__init__(*args, **kwargs)
