from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf.file import FileField, FileAllowed
from techblog.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message='Not a valid email address.')])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

    def check_email(self, field):
        return True if User.query.filter_by(email=field).first() else False


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[Email(message='Not a valid email address.'), Length(min=6, max=35)])
    username = StringField('Username', validators=[Length(min=5, max=35)])
    password = PasswordField('Password', validators=[EqualTo('pass_confirm', message = 'Password must match!'), Length(min=8, max=35)])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_email(self, field):
        return True if User.query.filter_by(email=field).first() else False

    def check_username(self, field):
        return True if User.query.filter_by(username=field).first() else False


class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators=[Email(message='Not a valid email address.'), Length(min=6, max=35)])
    username = StringField('Username', validators=[Length(min=5, max=35)])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def check_email(self, field):
        return True if User.query.filter_by(email=field).first() else False

    def check_username(self, field):
        return True if User.query.filter_by(username=field).first() else False