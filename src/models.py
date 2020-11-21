from app import db,ma

class User(db.Model):
  id=db.Column(db.Integer, primary_key=True)
  public_id=db.Column(db.String(50), unique=True)
  name=db.Column(db.String(50))
  email=db.Column(db.String(128))
  username=db.Column(db.String(50))
  password=db.Column(db.String(100))
  avatar=db.Column(db.String(512))
  admin=db.Column(db.Boolean)

  def __init__(self, public_id,name,email,username,password,avatar,admin):
    self.public_id=public_id
    self.name=name
    self.email=email 
    self.username=username
    self.password=password
    self.avatar=avatar
    self.admin=admin

class Todo(db.Model):
  id=db.Column(db.Integer, primary_key=True)
  content=db.Column(db.String(512))
  done=db.Column(db.Boolean)
  user_id=db.Column(db.Integer)

  def __init__(self, content,done,user_id):
    self.content=content
    self.done=done
    self.user_id=user_id


db.create_all()


class UserSchema(ma.Schema):
  class Meta:
    fields = ('id','public_id','name','email','username','password','avatar','admin')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class TodoShema(ma.Schema):
  class Meta:
    fields = ('id','content','done','user_id')


todo_schema = TodoShema()
todos_schema = TodoShema(many=True)

  


