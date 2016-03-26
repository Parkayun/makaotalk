from flask_socketio import emit, join_room

from .. import socketio
from ..models import db
from ..models.chat import Message


@socketio.on('join')
def join(data):
    username, room = data['username'], data['room']
    join_room(room)


@socketio.on('chat')
def chat(data):
    username, message_text, room = data['username'], data['message'], data['room']
    message = Message(username, message_text, int(room))
    db.session.add(message)
    db.session.commit()
    emit('response', {'username': username, 'message': {'id': message.id, 'text': message.text}}, room=room)
