from flask_socketio import join_room, send, emit

from .. import socketio


@socketio.on('join')
def join(data):
    print(data)
    username = data['username']
    room = data['room']
    join_room(room)
    emit('response', {'a': username + ' joined'}, room=room)
