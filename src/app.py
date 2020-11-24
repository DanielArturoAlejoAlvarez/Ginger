from config.config import *

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_marshmallow import Marshmallow

import os

app=Flask(__name__)

basedir=os.path.abspath(os.path.dirname(__file__))

# Configure DB 
app.config['SECRET_KEY']=SECRET_KEY
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# Models and Schema
db=SQLAlchemy(app)
ma=Marshmallow(app)

# Generate Tables in DB
db.create_all()

# All Controllers
from controllers.LoginController import *
from controllers.UserController import *
from controllers.TodoController import *