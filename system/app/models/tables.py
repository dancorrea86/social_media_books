from app import app
from app import db

readings = db.Table('readings', 
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('book_id', db.Integer, db.ForeignKey('book.book_id'))
)

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    readings = db.relationship('Book', secondary=readings, backref=db.backref('user', lazy='dynamic'))

class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String)
    readers = db.relationship('User', secondary=readings, backref=db.backref('book', lazy='dynamic'))
