from flask import Blueprint, request, session
from werkzeug.security import generate_password_hash, check_password_hash

from app.module_users.models import User
from app import db

users = Blueprint('users', __name__, url_prefix='/users')

@users.route("/")
def home():
    return "User module"

@users.route("/signup", methods=['POST'])
def add_user():
    content = request.json
    if not content: return "not json request", 400 # check json contains the keys 
    name = content.get('name')
    email = content.get('email')
    password = content.get('password')

    if not name or not email or not password: return "bad request", 400 # check json contains the keys 
    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database
    if user: return f"Email {email} already exists in database", 400 

    # create a new user with de json data 
    new_user = User(name=name, email=email, password=generate_password_hash( password, method='sha256') )

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return "saving user", 200

@users.route("/login", methods=['POST'])
def login_post():
    content = request.json
    if not content: return "not json request", 400 # check json contains the keys 
    email = content.get('email')
    password = content.get('password')

    if not email or not password: return "bad request", 400 # check json contains the keys 
    user = User.query.filter_by(email=email).first() # get user by email
    name = user.name
    password_hash = user.password

    if not user or not check_password_hash(password_hash, password):
        return F"email or password is incorrect", 403 # forbidden 

    # if the above check passes, then we know the user has the right credentials
    # start session with user
    session["name"] = name

    return f"user {name} authorizated", 200

@users.route("/logout")
def logout():
    session.pop("name", None)
    return "user logout", 200
