from config.config import *

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_marshmallow import Marshmallow

from flask_cors import CORS

app=Flask(__name__)

CORS(app)

app.config['SECRET_KEY']=SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
ma=Marshmallow(app)

db.create_all()

from controllers.LoginController import *
from controllers.UserController import *
from controllers.TodoController import *


if __name__=='__main__':
  app.run(debug=True)