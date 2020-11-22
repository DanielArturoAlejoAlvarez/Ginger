from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_marshmallow import Marshmallow

from flask_cors import CORS

app=Flask(__name__)

CORS(app)

app.config['SECRET_KEY']='RXuwGX6syfZoZ4gi$y8fbkEtDgknmsAcpUyVQRmo'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Br1tney$2=@localhost/ginger_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
ma=Marshmallow(app)

db.create_all()

from controllers.LoginController import *
from controllers.UserController import *
from controllers.TodoController import *


if __name__=='__main__':
  app.run(debug=True)