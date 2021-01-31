from app import app
from app import db
from flask import Flask
from app.models.tables import User, Book
from flask import jsonify, render_template, request
from app.forms import SignUpForm, BookRegister, AlterUser
# from app import tables

@app.route("/")
@app.route("/home")
def index():
    return render_template('base.html')

@app.route('/newuser', methods=['GET', 'POST'])
def new_user():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        user = User(username=result['username'])
        db.session.add(user)
        db.session.commit()
        return render_template('showResult.html', operation="Usuário", result=result)
    return render_template('userRegister.html', form=form)

@app.route("/newbook", methods=['GET', 'POST'])
def new_book():
    form = BookRegister()
    if form.is_submitted():
        result = request.form
        book = Book(book_name=result['bookname'])
        db.session.add(book)
        db.session.commit()
        return render_template('showResult.html', operation="Livro", result=result)
    return render_template('bookRegister.html', form=form)

@app.route("/alteruser", methods=['GET', 'POST'])
def alter_user():
    form = AlterUser()
    if form.is_submitted():
        result = request.form
        user = User.query.get(result['user_id'])
        user.username = result['username']
        db.session.add(user)
        db.session.commit()
        return render_template('showResult.html', operation="Usuário alterado", result=result)
    return render_template('alterUser.html', form=form)


@app.route("/alterbook/<id>/<name>")
def alter_book(id, name):
    book = Book.query.get(id)
    book.book_name = name
    db.session.add(book)
    db.session.commit()
    return "<h1>Livro alterado com sucesso</h1>"

@app.route("/readebook/<iduser>/<idbook>")
def reade(iduser, idbook):
    user = User.query.get(iduser)
    book = Book.query.get(idbook)
    book.readers.append(user)
    db.session.commit()
    return "<h1>Livro lido</h1>"

@app.route('/page/<string:user>')
def page(user):
    print(user)
    user = User.query.filter_by(username=user).first()
    print (user)
    if user:
        books = user.readings
        listOfBooks = []
        for book in books:
            listOfBooks.append(book.book_name)
        return jsonify(listOfBooks)
    
    return "Usuário invalido"

# @app.route('/page/<string:user>')
# def page(user):
#     return 'User: ' + user

@app.route("/showusers")
def showreaders():
    users = User.query.all()
    return render_template('userResults.html', users=users)



#################################################################
#Primeira Versão com request na URL
#################################################################

# @app.route("/newuser/<name>")
# def new_user(name):
#     user = User(username=name)
#     db.session.add(user)
#     db.session.commit()
#     return "<h1>Usuário cadastrado com sucesso</h1>"

# @app.route("/newbook/<bookname>")
# def new_book(bookname):
#     book = Book(book_name=bookname)
#     db.session.add(book)
#     db.session.commit()
#     return "<h1>Livro cadastrado com sucesso</h1>"

# @app.route("/alteruser/<id>/<name>")
# def alter_book(id, name):
#     user = User.query.get(id)
#     user.username = name
#     db.session.add(user)
#     db.session.commit()
#     return "<h1>Usuário alterado com sucesso</h1>"

@app.route("/showreads")
def showreads():
    books = Book.query.filter(User.readings).all()
    listOfBooks = []
    for book in books:
        listOfBooks.append(book.book_name)
    return jsonify(listOfBooks)