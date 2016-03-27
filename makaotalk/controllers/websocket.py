from flask import session
from flask_socketio import emit, join_room

from .. import socketio
from ..models import db
from ..models.chat import Message


@socketio.on('chat')
def chat(data):
    """Websocket controller when users doing real-time chat.
    Save chat messages on db and broadcast them each others who joined chat room.

    :param data: Data dictionary of chat.

     - `username`: Message author's username.
     - `message`: Message content.
     - `room`: primary key of :class:`~makaotalk.models.chat.ChatRoom`.

    :type data: :class:`dict`
    """
    username, message_text, room = data['username'], data['message'], data['room']
    message = Message(username, message_text, int(room))
    db.session.add(message)
    db.session.commit()
    emit('response', {'username': username, 'message': {'id': message.id, 'text': message.text}}, room=room)


@socketio.on('delete')
def delete(data):
    """Websocket controller when users delete their own message.
    Delete chat message on db and broadcast each others who joined chat room.

    :param data: Data dictionary of chat.

     - `message_id`: primary key of :class:`~makaotalk.models.chat.Message`.
     - `room`: primary key of :class:`~makaotalk.models.chat.ChatRoom`.

    :type data: :class:`dict`
    """
    message_id = int(data['message_id'])
    message = Message.query.filter_by(id=message_id, username=session['username']).first()
    if message:
        db.session.delete(message)
        db.session.commit()
        emit('delete', {'message_id': message_id}, room=data['room'])


@socketio.on('join')
def join(data):
    """Websocket controller when users joined chat room.
    Doing join logic with specific chat room.

    :param data: Data dictionary of chat.

     - `username`: Message author's username.
     - `room`: primary key of :class:`~makaotalk.models.chat.ChatRoom`.

    :type data: :class:`dict`
    """
    username, room = data['username'], data['room']
    join_room(room)


@socketio.on('update')
def update(data):
    """Websocket controller when users modify their own message.
    Update chat message on db and broadcast each others who joined chat room.

    :param data: Data dictionary of chat.

     - `username`: Message author's username.
     - `message_id`: primary key of :class:`~makaotalk.models.chat.Message`.
     - `message`: Message content.
     - `room`: primary key of :class:`~makaotalk.models.chat.ChatRoom`.

    :type data: :class:`dict`
    """
    username, message_id, message_text, room = data['username'], int(data['message_id']), data['message'], data['room']
    message = Message.query.filter_by(id=message_id, username=session['username']).first()
    if message:
        message.text = data['message']
        db.session.add(message)
        db.session.commit()
        emit('update', {'username': username, 'message': {'id': message.id, 'text': message.text}}, room=room)
