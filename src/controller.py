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
      current_user=User.filter_by(public_id=data['public_id']).filter()

    except:
      return jsonify({'msg': 'Token is invalid!'}), 401

    return f(current_user, *args, **kwargs)

  return decorated


# User Controller
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
  admin=False

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


# Apply Authentication
@app.route('/login')
def login():
  auth=request.authorization 

  if not auth or not auth.username or not auth.password:
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

  user = User.filter_by(username=auth.username).first()

  if not user:
    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

  if check_password_hash(user.password, auth.password):
    token=jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])

    return jsonify({'token': token.decode('UTF-8')})

  return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})





# Todo Controller
@app.route('/todos', methods=['GET'])
def get_todos():
  todos=Todo.query.all()
  result = todo_schema.dump(todos)
  return jsonify(result)

@app.route('/todos/<id>', methods=['GET'])
def get_todo(id):
  todo=Todo.query.get(id)
  return todo_schema.jsonify(todo)

@app.route('/todos', methods=['POST'])
def create_todo():
  content=request.json['content']
  done=False
  user_id=request.json['user_id']
  

  new_todo=Todo(content,done,user_id)

  db.session.add(new_todo)
  db.session.commit()

  return todo_schema.jsonify(new_todo)


@app.route('/todos/<id>', methods=['PUT'])
def update_todo(id):
  todo=Todo.query.get(id)

  content=request.json['content']
  done=False
  user_id=request.json['user_id']

  todo.content=content
  todo.done=done
  todo.user_id=user_id


  db.session.commit()

  return todo_schema.jsonify(todo)


@app.router('/todos/<id>', methods=['DELETE'])
def delete_todo(id):
  todo=Todo.query.get(id)

  db.session.delete(todo)
  db.session.commit()

  return todo_schema.jsonify(todo)
