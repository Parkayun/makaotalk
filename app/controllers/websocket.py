from flask_socketio import emit, join_room

from .. import socketio


@socketio.on('join')
def join(data):
    username, room = data['username'], data['room']
    join_room(room)
    emit('response', {'message': username + ' joined'}, room=room)


@socketio.on('chat')
def chat(data):
    username, message, room = data['username'], data['message'], data['room']
    emit('response', {'message': username + ': ' + message}, room=room)
