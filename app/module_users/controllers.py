from flask import Blueprint, request
from app.module_users.models import User
from app import db

users = Blueprint('users', __name__, url_prefix='/users')

@users.route("/")
def home():
    return "User module"

@users.route("/create", methods=['POST'])
def add_user():
    content = request.json
    name = content.get('name')
    email = content.get('email')
    password = content.get('password')
    if not name or not email or not password: return "bad request", 400
    new_user = User(name, email, password)
    db.session.add(new_user)
    db.session.commit()
    return "saving user"