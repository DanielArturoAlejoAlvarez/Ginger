from app import *

from flask import request,jsonify
from models import *
from functools import wraps
import jwt

# Middleware
def token_required(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    token=None
    if 'x-access-token' in request.headers:
      token=request.headers['x-access-token']

    if not token:
      return jsonify({'msg': 'Token is missing!'}), 401

    try:
      data = jwt.decode(token, app.config['SECRET_KEY'])
      current_user=User.query.filter_by(public_id=data['public_id']).first()

    except:
      return jsonify({'msg': 'Token is invalid!'}), 401

    return f(current_user, *args, **kwargs)

  return decorated