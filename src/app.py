from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_marshmallow import Marshmallow

app=Flask(__name__)

app.config['SECRET_KEY']='RXuwGX6syfZoZ4gi$y8fbkEtDgknmsAcpUyVQRmo'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:Br1tney$2=@localhost/ginger_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
ma=Marshmallow(app)

from controller import *

if __name__=='__main__':
  app.run(debug=True)