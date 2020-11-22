from app import *

from flask import request,jsonify,make_response

from models import *

import uuid

import jwt

import datetime

from functools import wraps

from werkzeug.security import generate_password_hash, check_password_hash

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
@token_required
def create_user(current_user):
  if not current_user.admin:
    return jsonify({'msg': 'Cannot perform that function!'})

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
    token=jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

    return jsonify({'token': token.decode('UTF-8')})

  return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})


# Todo Controller
@app.route('/v1/todos', methods=['GET'])
@token_required
def get_todos(current_user):
  if not current_user.admin:
    return jsonify({'msg': 'Cannot perform that function!'})

  todos=Todo.query.all()
  result = todos_schema.dump(todos)
  return jsonify(result)

@app.route('/v1/todos/<id>', methods=['GET'])
@token_required
def get_todo(current_user, id):
  if not current_user.admin:
    return jsonify({'msg': 'Cannot perform that function!'})

  todo=Todo.query.get(id)
  return todo_schema.jsonify(todo)

@app.route('/v1/todos', methods=['POST'])
@token_required
def create_todo(current_user):
  if not current_user.admin:
    return jsonify({'msg': 'Cannot perform that function!'})

  content=request.json['content']
  done=False
  user_id=request.json['user_id']  

  new_todo=Todo(content,done,user_id)

  db.session.add(new_todo)
  db.session.commit()

  return todo_schema.jsonify(new_todo)

@app.route('/v1/todos/<id>', methods=['PUT'])
@token_required
def update_todo(current_user, id):
  if not current_user.admin:
    return jsonify({'msg': 'Cannot perform that function!'})

  todo=Todo.query.get(id)

  content=request.json['content']
  done=request.json['done']
  user_id=request.json['user_id']

  todo.content=content
  todo.done=done
  todo.user_id=user_id

  db.session.commit()

  return todo_schema.jsonify(todo)

@app.route('/v1/todos/<id>', methods=['DELETE'])
@token_required
def delete_todo(current_user, id):
  if not current_user.admin:
    return jsonify({'msg': 'Cannot perform that function!'})

  todo=Todo.query.get(id)

  db.session.delete(todo)
  db.session.commit()

  return todo_schema.jsonify(todo)
