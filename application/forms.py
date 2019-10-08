from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, IntegerField, StringField, validators, SelectField

class LoginForum(FlaskForm):
    """ login form filds """
    username = TextField('username', render_kw={"placeholder": "e-mail"})
    password = PasswordField('password', render_kw={"placeholder": "password"})
