# Flask + socketio communication, backend handling of sockets

from flask_socketio import emit, join_room, leave_room

from .functions import generate_id
from . import socketio
from flask import request
from .models import Chat, Chat_Members, Chatroom, Leaderboard, User
from . import db
from sqlalchemy import exc


@socketio.on('join')
def on_join(data):
    # joining a room
    room = data['room']
    if room != "request.sid":
        print(room)
    else:
        room = request.sid
    join_room(room)
    chat_members = Chat_Members(room_id=room, )
    chatroom = Chatroom(room_id=room, room_name=room)
    emit('joined', {'username': data['user_id'], 'room': room}, room=room)

@socketio.on('text')
def on_message(data):
    # sending a message
    room = data[room]
    if room == "request.sid":
        room = request.sid
    emit('message', {'username': data['username'], 'msg': data['msg']}, room=room)
    chat = Chat(chat_id = generate_id())
    db.session.add(chat)
    db.session.commit()

@socketio.on('leave')
def on_leave(data):
    # leaving a room
    username = data['username']
    room = data['room']
    leave_room(room)
    # emit('joined', {'username': data['username'], 'room': room}, room=room)

@socketio.on('leaderboard')
def leaderboard(data):
    # updating leaderboard
    username = data['username']
    score = data['score']
    new_leader = Leaderboard(1, score, User.username)
    db.session.add(new_leader)
    try:
        leaderboard = Leaderboard.query.order_by(score.desc())
        if len(leaderboard) >= 1:
            for user in leaderboard:
                if user.position < new_leader.position:
                    new_leader.position = user.position
                    user.position -= 1
    except exc.OperationalError:
        pass
    db.session.commit()