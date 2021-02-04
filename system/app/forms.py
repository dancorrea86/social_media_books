from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField

class SignUpForm(FlaskForm):
    username = StringField('Username')
    email = StringField('Email')
    submit = SubmitField('Submit')

class BookRegister(FlaskForm):
    bookname = StringField('Bookname')
    submit = SubmitField('Submit')

class AlterUser(FlaskForm):
    user_id = IntegerField('User_id')
    username = StringField('Username')
    submit = SubmitField('Submit')

class AlterBook(FlaskForm):
    book_id = IntegerField('Book_id')
    book_name = StringField('Book_name')
    submit = SubmitField('Submit')

class SearchUser(FlaskForm):
    user_id = IntegerField('User_id')
    submit = SubmitField('Submit')

class Showreader(FlaskForm):
    user_id = IntegerField('User_id')
    submit = SubmitField('Submit')