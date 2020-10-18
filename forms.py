from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, EqualTo, Length
from wtforms import PasswordField, StringField


class RegistrationForm(FlaskForm):
    """Registration Form"""

    username = StringField("Username", validators=[InputRequired(message="Username Required"), Length(
        min=4, max=25, message="Username must be between 4 and 25 characters")])
    password = PasswordField("Password", validators=[InputRequired(
        message="Username Required"), EqualTo('confirm', message="Passwords Do Not Match")])
    confirm = PasswordField("Confirm Password")
