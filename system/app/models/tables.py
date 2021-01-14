from app import app
from app import db

subs = db.Table('subs', 
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id')),
    db.Column('book_id', db.Integer, db.ForeignKey('book.book_id'))
)

class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    readings = db.relationship('Book', secondary=subs, backref=db.backref('readers', lazy='dynamic'))

    def __init__(self, username):
        self.username = username

    # def __repr__(self):
    #     return '<User %r>' % self.username

class Book(db.Model):
    __tablename__ = "book"

    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String)

    def __init__(self, book_name):
        self.book_name = book_name

    # def __repr__(self):
    #     return '<User %r>' % self.book_name