from app import *

from flask import request,jsonify

from models import *

import uuid 

from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/users', methods=['GET'])
def get_users():
  users=User.query.all()
  result = users_schema.dump(users)
  return jsonify(result)

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
  user=User.query.get(id)
  return user_schema.jsonify(user)

@app.route('/users', methods=['POST'])
def create_user():
  public_id=str(uuid.uuid4())
  name=request.json['nane']
  email=request.json['email']
  username=request.json['usernane']
  password=generate_password_hash(request.json['password'],method='sha256')
  avatar=request.json['avatar']
  admin=request.json['admin']

  new_user=User(public_id,name,email,username,password,avatar,admin)

  db.session.add(new_user)
  db.session.commit()

  return user_schema.jsonify(new_user)


@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
  user=User.query.get(id)

  public_id=str(uuid.uuid4())
  name=request.json['nane']
  email=request.json['email']
  username=request.json['usernane']
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


@app.router('/users/<id>', methods=['DELETE'])
def delete_user(id):
  user=User.query.get(id)

  db.session.delete(user)
  db.session.commit()

  return user_schema.jsonify(user)
