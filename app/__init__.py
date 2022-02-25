# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Import env vars
from dotenv import load_dotenv
from config import BASE_DIR
import os
load_dotenv(os.path.join(BASE_DIR, 'env', '.env'))

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Index Page
@app.route('/')
def index():
    return f"Welcome to API states {os.getenv('SECRET_KEY')} {os.getenv('MAPBOX_TOKEN')}", 200

# Import a module / component using its blueprint handler variable (mod_auth)
from app.module_users.controllers import users as users_module
from app.module_states.controllers import states as states_module

# Register blueprint(s)
app.register_blueprint(users_module)
app.register_blueprint(states_module)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()