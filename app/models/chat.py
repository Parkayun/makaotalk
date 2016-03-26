from . import db


class ChatRoom(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(50))
    created_at = db.Column(db.DateTime())

    messages = db.relationship('Message', backref='chat_room', lazy='dynamic')

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<ChatRoom %d - %r>' % (self.id, self.title)


class Message(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(20))
    text = db.Column(db.Text())
    created_at = db.Column(db.DateTime())

    chat_room_id = db.Column(db.Integer(), db.ForeignKey('chat_room.id'))

    def __init__(self, username, text, chat_room_id):
        self.title, self.text, self.chat_room_id = username, text, chat_room_id

    def __repr__(self):
        return '<Message %d - %s: %s (ChatRoom: %d)>' % (self.id, self.username, self.text, self.chat_room_id)
