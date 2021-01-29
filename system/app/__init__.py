from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'

# Configuration Flask SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from .controllers import default
from .models import tables