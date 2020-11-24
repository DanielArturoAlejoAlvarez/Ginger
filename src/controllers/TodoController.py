from app import app
from flask import request,jsonify
from models.Todo import *
from middlewares.authentication import *

# Todo Controller
@app.route('/v1/todos', methods=['GET'])
@token_required
def get_todos(current_user):
  if not current_user.admin:
    return jsonify({'msg': 'Cannot perform that function!'})

  todos=Todo.query.filter_by(user_id=current_user.id).all()
  result = todos_schema.dump(todos)
  return jsonify(result)

@app.route('/v1/todos/<id>', methods=['GET'])
@token_required
def get_todo(current_user, id):
  if not current_user.admin:
    return jsonify({'msg': 'Cannot perform that function!'})

  todo=Todo.query.filter_by(id=id, user_id=current_user.id).first()
  if not todo:
    return jsonify({'msg': 'No todo found!'})
    
  return todo_schema.jsonify(todo)

@app.route('/v1/todos', methods=['POST'])
@token_required
def create_todo(current_user):
  if not current_user.admin:
    return jsonify({'msg': 'Cannot perform that function!'})

  title=request.json['title']
  content=request.json['content']
  done=False
  user_id=current_user.id  

  new_todo=Todo(title,content,done,user_id)

  db.session.add(new_todo)
  db.session.commit()

  return todo_schema.jsonify(new_todo)

@app.route('/v1/todos/<id>', methods=['PUT'])
@token_required
def update_todo(current_user, id):
  if not current_user.admin:
    return jsonify({'msg': 'Cannot perform that function!'})

  todo=Todo.query.filter_by(id=id, user_id=current_user.id).first()

  if not todo:
    return jsonify({'msg': 'No todo found!'})

  title=request.json['title']
  content=request.json['content']
  done=request.json['done']
  user_id=current_user.id

  todo.title=title
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

  todo=Todo.query.filter_by(id=id, user_id=current_user.id).first()

  if not todo:
    return jsonify({'msg': 'No todo found!'})

  db.session.delete(todo)
  db.session.commit()

  return todo_schema.jsonify(todo)