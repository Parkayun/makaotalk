from flask import render_template

from . import blueprint
from ..models.chat import ChatRoom


@blueprint.route('/')
def index():
    chat_rooms = ChatRoom.query.all()
    data = {'chat_rooms': chat_rooms}
    return render_template('chat/index.html', **data)
