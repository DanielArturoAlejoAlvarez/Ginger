from app import db,ma
from datetime import datetime

class Todo(db.Model):
  id=db.Column(db.Integer, primary_key=True)
  content=db.Column(db.String(512))
  done=db.Column(db.Boolean)
  user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  user=db.relationship('User', backref=db.backref('todos', lazy=True))


  def __init__(self,title,content,done,user_id):
    self.title=title
    self.content=content
    self.done=done
    self.user_id=user_id

  def __repr__(self):
    return '<Todo> %r' % self.title

# Generate Tables in DB
db.create_all()


class TodoSchema(ma.Schema):
  class Meta:
    fields = ('id','title','content','done','user_id')


todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)