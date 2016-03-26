from . import db


class ChatRoom(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(50))
    created_at = db.Column(db.DateTime())

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return '<ChatRoom %d - %r>' % (self.id, self.title)
