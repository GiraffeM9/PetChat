# Database Models created via sqlalchemy, inherits from db.Model class
# flask_login to allow the User model to be loaded into cookies

from sqlalchemy import ForeignKey
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_joined = db.Column(db.DateTime(timezone=True), default=func.now())


class Pet(db.Model):
    __tablename__ = 'Pet'
    pet_id = db.Column(db.Integer, primary_key=True, unique=True)
    owner_id = db.Column(db.Integer, ForeignKey(User.id), unique=True)
    hunger = db.Column(db.Integer)
    energy = db.Column(db.Integer)
    cleanliness = db.Column(db.Integer)


class Chat(db.Model):
    __tablename__ = 'Chat'
    chat_id = db.Column(db.Integer, primary_key=True, unique=True)
    sender_id = db.Column(db.Integer, ForeignKey(User.id))
    timestamp = db.Column(db.DateTime(timezone=True), default=func.now())


class Chatroom(db.Model):
    __tablename__ = 'Chatroom'
    room_id = db.Column(db.Integer, ForeignKey(Chat.chat_id), primary_key=True, unique=True)
    room_name = db.Column(db.String(20), unique=True)


class Chat_Members(db.Model):
    __tablename__ = 'Chat_Members'
    room_id = db.Column(db.Integer, ForeignKey(Chatroom.room_id), primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey(User.id), primary_key=True)


class Leaderboard(db.Model):
    __tablename__ = 'Leaderboard'
    position = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)
    username = db.Column(db.String, ForeignKey(User.username), primary_key=True)
