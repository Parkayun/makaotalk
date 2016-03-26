from . import db


class ChatRoom(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(50))
    created_at = db.Column(db.DateTime())
