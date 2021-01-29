from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField

class SignUpForm(FlaskForm):
    username = StringField('Username')
    submit = SubmitField('Submit')

class BookRegister(FlaskForm):
    bookname = StringField('Bookname')
    submit = SubmitField('Submit')

class AlterUser(FlaskForm):
    user_id = IntegerField('User_id')
    username = StringField('Username')
    submit = SubmitField('Submit')