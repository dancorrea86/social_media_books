from app import app
from app import db
from flask import Flask
from app.models.tables import User, Book
# from app import tables

@app.route("/")
@app.route("/home")
def index():
    return "<h1>Bem Vindo ao Projeto</h1>"


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

@app.route("/readebook/<iduser>/<idbook>")
def reade(iduser, idbook):
    user = User.query.get(iduser)
    book = Book.query.get(idbook)
    book.readers.append(user)
    db.session.commit()
    return "<h1>Livro lido</h1>"

@app.route("/showreads/<iduser>")
def showreaders(iduser):
    print(User.query.with_parent(1))

    return f'<h1>Livro lido44</h1>'