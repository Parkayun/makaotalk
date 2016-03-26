from flask import session
from flask_socketio import emit, join_room

from .. import socketio
from ..models import db
from ..models.chat import Message


@socketio.on('chat')
def chat(data):
    username, message_text, room = data['username'], data['message'], data['room']
    message = Message(username, message_text, int(room))
    db.session.add(message)
    db.session.commit()
    emit('response', {'username': username, 'message': {'id': message.id, 'text': message.text}}, room=room)


@socketio.on('delete')
def delete(data):
    message_id = int(data['message_id'])
    message = Message.query.filter_by(id=message_id, username=session['username']).first()
    if message:
        db.session.delete(message)
        db.session.commit()
        emit('delete', {'message_id': message_id}, room=data['room'])


@socketio.on('join')
def join(data):
    username, room = data['username'], data['room']
    join_room(room)


@socketio.on('update')
def update(data):
    username, message_id, message_text, room = data['username'], int(data['message_id']), data['message'], data['room']
    message = Message.query.filter_by(id=message_id, username=session['username']).first()
    if message:
        message.text = data['message']
        db.session.add(message)
        db.session.commit()
        emit('update', {'username': username, 'message': {'id': message.id, 'text': message.text}}, room=room)
