# GINGER REST API

## Description

This repository is a Software of Development with Python.

## Virtual

Using pipenv preferably.

## Installation

Using Flask, SQLAlchemy, Marshmallow preferably.

## DataBase

Using SQLite3, PostgreSQL MySQL, MongoDB,etc.

## Apps

Using Postman, Insomnia, Talend API Tester,etc.

```html
[x-access-token]: [TOKEN] (headers client rest)
```

## Usage

```html
$ git clone https://github.com/DanielArturoAlejoAlvarez/Ginger.git [NAME APP] $
pipenv shell $ pipenv python src/app.py
```

Follow the following steps and you're good to go! Important:

![alt text](https://community.gitpod.io/uploads/default/original/1X/744caf335f006bca50389d73d873afb25bf478ce.gif)

## Coding

### Config

```python
DATABASE_URI='mysql+pymysql://{}:{}@{}/{}'.format(DB_USER,DB_PASSWORD,DB_HOST,DB_NAME)
```

### Authentication

```python
...
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

...
````

### Middlewares

```python
...
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
...
```

### Models

```python
...
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
...
```

### Controllers

```python
...
@app.route('/v1/users', methods=['GET'])
def get_users():
  users=User.query.all()
  result = users_schema.dump(users)
  return jsonify(result)

@app.route('/v1/users/<id>', methods=['GET'])
def get_user(id):
  user=User.query.get(id)
  return user_schema.jsonify(user)

@app.route('/v1/users', methods=['POST'])
def create_user():
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
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/DanielArturoAlejoAlvarez/Ginger. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).

```

```
