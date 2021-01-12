from app import app
from app import db
from flask import Flask
from app.models.tables import User
# from app import tables

@app.route("/")
@app.route("/home")
def index():
    return "Bem Vindo ao Projeto"


@app.route("/newuser/<name>")
def new_user(name):
    user = User(name=name, username="daniel", password=1234, email="danielm@")
    db.session.add(user)
    db.session.commit()
    return "<h1>Usuário cadastrado com sucesso</h1>"

