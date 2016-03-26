from flask import render_template, request, redirect, url_for

from . import blueprint
from ..models import db
from ..models.chat import ChatRoom


@blueprint.route('/chat/<int:room_id>/')
def chat(room_id):
    chat_room = ChatRoom.query.get_or_404(room_id)
    data = {'chat_room': chat_room}
    return render_template('chat/chat.html', **data)


@blueprint.route('/chat/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form.get('title', '')
        if title != '':
            chat_room = ChatRoom(title)
            db.session.add(chat_room)
            db.session.commit()
            return redirect(url_for('controllers.index'))
    return render_template('chat/create.html')


@blueprint.route('/')
def index():
    chat_rooms = ChatRoom.query.all()
    data = {'chat_rooms': chat_rooms}
    return render_template('chat/index.html', **data)
