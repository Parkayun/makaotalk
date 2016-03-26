from flask_socketio import emit, join_room

from .. import socketio


@socketio.on('join')
def join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    emit('response', {'message': username + ' joined'}, room=room)
