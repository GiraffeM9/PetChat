# Database Models created via sqlalchemy, 
# flask_login to allow the User model to be loaded into cookies

from sqlalchemy import ForeignKey
from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func


class Chatroom(db.Model):
    __tablename__ = 'Chatroom'
    room_id = db.Column(db.Integer, primary_key=True, unique=True)
    room_name = db.Column(db.String(20), unique=True)
    capacity = db.Column(db.Integer)
    full = db.Column(db.Boolean)

class Chat(db.Model):
    __tablename__ = 'Chat'
    chat_id = db.Column(db.Integer, primary_key=True, unique=True)
    #user_a = db.Column()


class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_joined = db.Column(db.DateTime(timezone=True), default=func.now())


class Item(db.Model):
    __tablename__ = 'Item'
    item_id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String)
    price = db.Column(db.Float)


class Inventory(db.Model):
    __tablename__ = 'Inventory'
    inventory_id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, ForeignKey(Item.item_id), primary_key=True)
    amount = db.Column(db.Integer)


