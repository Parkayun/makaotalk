import os, sys; sys.path.insert(0, os.path.abspath('..'));

from . import get_app
from makaotalk.models import db
from makaotalk.models.chat import ChatRoom, Message


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


def test_message():
    Message.query.delete()
    ChatRoom.query.delete()

    _chat_room = ChatRoom('test')
    db.session.add(_chat_room)
    db.session.commit()

    assert Message.query.count() == 0

    username, text, chat_room_id = 'tester', 'test', _chat_room.id
    _message = Message(username, text, chat_room_id)
    db.session.add(_message)
    db.session.commit()

    assert Message.query.count() == 1
    assert _message.username == username
    assert _message.text == text
    assert _message.chat_room_id == chat_room_id

    message = Message.query.first()

    assert _message.id == message.id
    assert _message.text == message.text
    assert _message.chat_room_id == message.chat_room_id
    assert _message.created_at == message.created_at
