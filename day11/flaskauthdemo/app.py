from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from uuid import uuid4
import jwt
import datetime
from functools import wraps
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'PUBLICINSECURESECRET')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     public_id = db.Column(db.Integer)
     name = db.Column(db.String(50))
     password = db.Column(db.String(50))
     admin = db.Column(db.Boolean)

class Author(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(50), unique=True, nullable=False)
     book = db.Column(db.String(20), unique=True, nullable=False)
     country = db.Column(db.String(50), nullable=False)
     booker_prize = db.Column(db.Boolean)
     user_id = db.Column(db.Integer)

def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
            print(data)
            current_user = User.query.filter_by(
                public_id=data['public_id']
            ).first()
        except:
            return jsonify({'message': 'token is invalid'})

        return f(current_user, *args, **kwargs)
    
    return wrapper


@app.route('/register', methods=['GET', 'POST'])
def signup_user():
    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(public_id=str(uuid4()), name=data['name'],  password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'registered successfully'})


@app.route('/login', methods=['GET', 'POST'])
def login_user():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})

    user = User.query.filter_by(name=auth.username).first()

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token': token})

    return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})


@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()

    result = []

    for user in users:
        user_data = {}
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['admin'] = user.admin

        result.append(user_data)

    return jsonify({'users': result})


@app.route('/authors', methods=['POST'])
@token_required
def create_author(current_user):
    data = request.get_json()

    new_author = Author(
        name=data['name'],
        country=data['country'],
        book=data['book'],
        booker_prize=True,
        user_id=current_user.id,
    )
    db.session.add(new_author)
    db.session.commit()

    return jsonify({'message': 'new author created'})


@app.route('/author')
@token_required
def get_authors(current_user):
    authors = Author.query.filter_by(user_id=current_user.id).all()

    result = []

    for author in authors:
        author_data = {}
        author_data['name'] = author.name
        author_data['book'] = author.book
        author_data['country'] = author.country
        author_data['booker_prize'] = author.booker_prize
        result.append(author_data)

    return jsonify({'list_of_authors': result})


@app.route('/authors/<author_id>', methods=['DELETE'])
@token_required
def delete_author(current_user, author_id):
    author = Author.query.filter_by(id=author_id, user_id=current_user.id).first()

    if not author:
        return jsonify({'message': 'author does not exist'}), 404
    
    db.session.delete(author)
    db.session.commit()

    return jsonify({'message': 'Author delete'})
