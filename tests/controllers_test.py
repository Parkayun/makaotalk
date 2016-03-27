import os, sys; sys.path.insert(0, os.path.abspath('..'));

from . import get_app
from makaotalk.models import db
from makaotalk.models.chat import ChatRoom, Message


app = get_app('sqlite:///../test.db')
client = app.test_client()


def test_web_index():
    Message.query.delete()
    ChatRoom.query.delete()

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
