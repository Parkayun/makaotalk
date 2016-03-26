from flask_socketio import emit, join_room

from .. import socketio
from ..models import db
from ..models.chat import Message


@socketio.on('join')
def join(data):
    username, room = data['username'], data['room']
    join_room(room)
    emit('response', {'message': username + ' joined'}, room=room)


@socketio.on('chat')
def chat(data):
    username, message, room = data['username'], data['message'], data['room']
    db.session.add(Message(username, message, int(room)))
    db.session.commit()
    emit('response', {'message': username + ': ' + message}, room=room)
