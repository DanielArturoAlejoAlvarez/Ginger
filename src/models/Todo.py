from app import db,ma

class Todo(db.Model):
  id=db.Column(db.Integer, primary_key=True)
  content=db.Column(db.String(512))
  done=db.Column(db.Boolean)
  user_id=db.Column(db.Integer)

  def __init__(self, content,done,user_id):
    self.content=content
    self.done=done
    self.user_id=user_id


class TodoSchema(ma.Schema):
  class Meta:
    fields = ('id','content','done','user_id')


todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)