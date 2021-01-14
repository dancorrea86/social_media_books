from app import app
from app import db
from flask import Flask
from app.models.tables import User, Book
# from app import tables

@app.route("/")
@app.route("/home")
def index():
    return "Bem Vindo ao Projeto"


@app.route("/newuser/<name>")
def new_user(name):
    user = User(username=name)
    db.session.add(user)
    db.session.commit()
    return "<h1>Usuário cadastrado com sucesso</h1>"

@app.route("/newbook/<bookname>")
def new_book(bookname):
    book = Book(book_name=bookname)
    db.session.add(book)
    db.session.commit()
    return "<h1>Livro cadastrado com sucesso</h1>"

@app.route("/alteruser/<id>/<name>")
def alter_user(id, name):
    user = User.query.get(id)
    user.username = name
    db.session.add(user)
    db.session.commit()
    return "<h1>Usuário alterado com sucesso</h1>"