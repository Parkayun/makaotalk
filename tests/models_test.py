import os, sys; sys.path.insert(0, os.path.abspath('..'));

from . import get_app
from makaotalk.models import db
from makaotalk.models.chat import ChatRoom


app = get_app('sqlite:///../test.db')


def test_chat_room():
    ChatRoom.query.delete()

    assert ChatRoom.query.count() == 0

    _chat_room = ChatRoom('test')
    db.session.add(_chat_room)
    db.session.commit()

    assert  ChatRoom.query.count() == 1

    chat_room = ChatRoom.query.first()

    assert _chat_room.id == chat_room.id
    assert _chat_room.title == chat_room.title
    assert _chat_room.created_at == chat_room.created_at
