from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from cobochat.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    full_name = StringField('Full Name',
                        validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=100)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password'), Length(min=2, max=100)])
    account_type = SelectField('Account Type', validators=[DataRequired()], 
                               choices=['User', 'Administrator', 'Networking Engineer', 'Owner'])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    full_name = StringField('Full Name',
                        validators=[DataRequired(), Length(min=2, max=20)])
    bio = TextAreaField('Bio')
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'webp'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')
            
class OTPSetup(FlaskForm):
    OTPCode = StringField("6 digit authenticator code",
                          validators=[DataRequired, Length(min=6, max=6)])
            
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=100)])
    content = TextAreaField('Content', validators=[DataRequired(), Length(min=1, max=1000)])
    post_image = FileField('Upload Picture', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'webp'])])
    submit = SubmitField('Post')

class AnnouncementForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class Like(FlaskForm):
    submit = SubmitField('Like')