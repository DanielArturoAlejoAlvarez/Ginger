from app import *

from flask import request,jsonify,make_response

from models import *

import jwt

import datetime

from werkzeug.security import check_password_hash


# Apply Authentication
@app.route('/login')
def login():
  auth=request.authorization 

  if not auth or not auth.username or not auth.password:
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

  user = User.query.filter_by(username=auth.username).first()

  if not user:
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

  if check_password_hash(user.password, auth.password):
    token=jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)}, app.config['SECRET_KEY'])

    return jsonify({'token': token.decode('UTF-8')})

  return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})



