from flask_wtf import wtforms
from wtforms import StringField, IntegerField, SubmitField, BooleanField, form, FileField, PasswordField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import User
from flaskblog.models import User


class RegistrationForm(form):
    team_name = StringField('Team Name',
                            validators=[DataRequired(), Length(min=1, max=40)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    phone_number = IntegerField('Password', validators=[DataRequired()])

    upload1 = BooleanField('Student')
    upload2 = BooleanField('Professional')
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'doc', 'pdf'])])
    submit1 = SubmitField('Upload')
    submit = SubmitField('Register')

    def validate_team_name(self, team_name):
        user = User.query.filter_by(team_name=team_name.data).first()
        if user:
            raise ValidationError('That name is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

        def validate_phone_number(self, phone_number):
            user = User.query.filter_by(phone_number=phone_number.data).first()
            if user:
                raise ValidationError('That phone number is taken. Please choose a different one.')


class LoginForm(form):
    username = StringField('Username',
                           validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Login')


class RequestResetForm(form):
    username = StringField('Username',
                           validators=[DataRequired()])
    submit = SubmitField('Request Password Reset')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')


class ResetPasswordForm(form):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')
