# Flask + socketio communication, backend handling of sockets

from flask_socketio import emit, join_room, leave_room
from . import socketio
from flask import request

@socketio.on('join')
def on_join(data):
    room = data['room']
    if room != "request.sid":
        print(room)
    else:
        room = request.sid
    join_room(room)
    emit('joined', {'username': data['username'], 'room': room}, room=room)

@socketio.on('text')
def on_message(data):
    room = data[room]
    if room == "request.sid":
        room = request.sid
    emit('message', {'username': data['username'], 'msg': data['msg']}, room=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    # emit('joined', {'username': data['username'], 'room': room}, room=room)