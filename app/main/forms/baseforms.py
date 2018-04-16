from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms import ValidationError


class LoginForm(FlaskForm):
    userName = StringField('UserName', validators=[DataRequired(), Length(5, 20)])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("RememberMe")
    submit = SubmitField('Log In')