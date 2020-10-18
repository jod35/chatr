from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, EqualTo, Length,ValidationError
from wtforms import PasswordField, StringField
from .models import User

def invalid_credentials(form,field):
    """Username and Password Cheker"""
    username_entered=form.username.data

    password_entered=form.password.data

    # check if user is valid

    user_obj=User.query.filter_by(username=username_entered).first()

    if user_obj is None:
        raise ValidationError("Invalid username or password")

    elif password_entered != user_obj.password:
        raise ValidationError("Invalid username or password")



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



class LoginForm(FlaskForm):
    """Login Form"""
    username = StringField("Username", validators=[InputRequired(message="Username Required")])

    password = PasswordField("Password",validators=[InputRequired(message="Password Required"),invalid_credentials])

    
