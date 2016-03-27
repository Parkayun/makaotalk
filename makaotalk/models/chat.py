from . import db


class ChatRoom(db.Model):
    """ChatRoom contains general information for chat.
    Chats are categorized according to id (primary key).
    Each ChatRoom has many of Message(One to Many relationship) .

    :param title: title of chat room.
    :type title: :class:`str`
    """
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(50))
    created_at = db.Column(db.DateTime())

    messages = db.relationship('Message', backref='chat_room', lazy='dynamic')

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<ChatRoom %d - %r>' % (self.id, self.title)


class Message(db.Model):
    """Message contains general information.
    Message has dependency with ChatRoom(Many To One relationship).
    """
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(20))
    text = db.Column(db.Text())
    created_at = db.Column(db.DateTime())

    chat_room_id = db.Column(db.Integer(), db.ForeignKey('chat_room.id'))

    def __init__(self, username, text, chat_room_id):
        self.username, self.text, self.chat_room_id = username, text, chat_room_id

    def __repr__(self):
        return '<Message %d - %s: %s (ChatRoom: %d)>' % (self.id, self.username, self.text, self.chat_room_id)
