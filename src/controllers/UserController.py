from app import app
from flask import request,jsonify
from models.User import *
from middlewares.authentication import *
from werkzeug.security import generate_password_hash
import uuid

# User Controller
@app.route('/v1/users', methods=['GET'])
@token_required
def get_users(current_user):

  if not current_user.admin:
    return jsonify({'msg': 'Cannot perform that function!'})

  users=User.query.all()
  result = users_schema.dump(users)
  return jsonify(result)

@app.route('/v1/users/<id>', methods=['GET'])
@token_required
def get_user(current_user, id):
  if not current_user.admin:
    return jsonify({'msg': 'Cannot perform that function!'})

  user=User.query.get(id)
  return user_schema.jsonify(user)

@app.route('/v1/users', methods=['POST'])
#@token_required
def create_user():
  # if not current_user.admin:
  #   return jsonify({'msg': 'Cannot perform that function!'})

  public_id=str(uuid.uuid4())
  name=request.json['name']
  email=request.json['email']
  username=request.json['username']
  password=generate_password_hash(request.json['password'],method='sha256')
  avatar=request.json['avatar']
  admin=False

  new_user=User(public_id,name,email,username,password,avatar,admin)

  db.session.add(new_user)
  db.session.commit()

  return user_schema.jsonify(new_user)

@app.route('/v1/users/<id>', methods=['PUT'])
@token_required
def update_user(current_user, id):
  if not current_user.admin:
    return jsonify({'msg': 'Cannot perform that function!'})

  user=User.query.get(id)

  public_id=str(uuid.uuid4())
  name=request.json['name']
  email=request.json['email']
  username=request.json['username']
  password=generate_password_hash(request.json['password'],method='sha256')
  avatar=request.json['avatar']
  admin=request.json['admin']

  user.public_id=public_id
  user.name=name
  user.email=email
  user.username=username
  user.password=password
  user.avatar=avatar
  user.admin=admin

  db.session.commit()

  return user_schema.jsonify(user)

@app.route('/v1/users/<id>', methods=['DELETE'])
@token_required
def delete_user(current_user, id):
  if not current_user.admin:
    return jsonify({'msg': 'Cannot perform that function!'})

  user=User.query.get(id)

  db.session.delete(user)
  db.session.commit()

  return user_schema.jsonify(user)