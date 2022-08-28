# Initalises database, builds flask app (backend), loads socket functions and other flask functions

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_socketio import SocketIO

from .functions import *

db = SQLAlchemy()
DB_NAME = "PetChat.db"
# initalises database connection and name

app = Flask(__name__)
app.config['SECRET_KEY'] = "helloworld"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
# configuration for backend
socketio = SocketIO(app, manage_session=False)
# initalises socket for user

def page_not_found(e):
    # error handling page
  return render_template('404.html'), 404

def create_app():
    # initialises whole application
    db.init_app(app)

    from .models import User

    # loads flask routes 
    from .auth import auth
    from .views import views
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(views, url_prefix="/")

    create_db(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    # loads socketio events to communicate with javascript socketio events
    from .events import on_leave, on_join, on_message, leaderboard
    
    # loads error handeler
    app.register_error_handler(404, page_not_found)

    return app, socketio

def create_db(app):
    # checks if database file exists already, if not creates one
    if not path.exists(f"website/{DB_NAME}"):
        db.create_all(app=app)
        print("Created database")
