# Initalises database, builds flask app (backend), loads socket functions and other flask functions

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_socketio import SocketIO
from .functions import *

db = SQLAlchemy()
DB_NAME = "PetChat.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = "helloworld"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
socketio = SocketIO(app, manage_session=False)

def page_not_found(e):
  return render_template('404.html'), 404

def create_app():
    db.init_app(app)

    from .models import User
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

    from .events import on_leave, on_join, on_message
    
    app.register_error_handler(404, page_not_found)

    return app, socketio

def create_db(app):
    if not path.exists(f"website/{DB_NAME}"):
        db.create_all(app=app)
        print("Created database")
