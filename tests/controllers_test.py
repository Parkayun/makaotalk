import os, sys; sys.path.insert(0, os.path.abspath('..'))

from . import get_app
from makaotalk.models import db
from makaotalk.models.chat import ChatRoom, Message


app = get_app('sqlite:///../test.db')
client = app.test_client()


def setup_function(_):
    Message.query.delete()
    ChatRoom.query.delete()


def test_web_index():
    title = 'test'

    resp = client.get('/')
    assert title.encode('utf-8') not in resp.data
    assert resp.status_code == 200

    chat_room = ChatRoom(title)
    db.session.add(chat_room)
    db.session.commit()

    resp = client.get('/')
    assert title.encode('utf-8') in resp.data
    assert resp.status_code == 200


def test_web_chat_create():
    title = 'create_test'

    assert ChatRoom.query.filter_by(title=title).count() == 0

    resp = client.post('/chat/create/', data={'title': title})
    assert resp.status_code == 302
    assert ChatRoom.query.filter_by(title=title).count() == 1


def test_web_chat_room():
    title = 'room_test'
    chat_room = ChatRoom(title)

    resp = client.get('/chat/%s/' % chat_room.id)
    assert resp.status_code == 404

    db.session.add(chat_room)
    db.session.commit()

    username, text = 'tester', 'test-text'
    message = Message(username, text, chat_room.id)

    resp = client.get('/chat/%s/' % chat_room.id)
    assert title.encode('utf-8') in resp.data
    assert  username.encode('utf-8') not in resp.data
    assert text.encode('utf-8') not in resp.data
    assert resp.status_code == 200

    db.session.add(message)
    db.session.commit()

    resp = client.get('/chat/%s/' % chat_room.id)
    assert title.encode('utf-8') in resp.data
    assert username.encode('utf-8') in resp.data
    assert text.encode('utf-8') in resp.data
    assert resp.status_code == 200
