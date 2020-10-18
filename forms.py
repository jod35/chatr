from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, EqualTo, Length,ValidationError
from wtforms import PasswordField, StringField
from models import User


class RegistrationForm(FlaskForm):
    """Registration Form"""

    username = StringField("Username", validators=[InputRequired(message="Username Required"), Length(
        min=4, max=25, message="Username must be between 4 and 25 characters")])
    password = PasswordField("Password", validators=[InputRequired(
        message="Username Required"), EqualTo('confirm', message="Passwords Do Not Match")])
    confirm = PasswordField("Confirm Password")

    def validate_username(self,username):
        user_obj=User.query.filter_by(username=username.data).first()

        if user_obj:
            raise ValidationError(f"{username.data} is already taken")




