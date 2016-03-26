from flask import jsonify, render_template, request, redirect, session, url_for
from sqlalchemy.orm.exc import UnmappedInstanceError

from . import blueprint
from ..models import db
from ..utils.decorators import get_or_set_username
from ..models.chat import ChatRoom, Message


@blueprint.route('/chat/<int:room_id>/')
@get_or_set_username
def chat(room_id):
    chat_room = ChatRoom.query.get_or_404(room_id)
    messages = Message.query.filter_by(chat_room=chat_room)
    data = {'chat_room': chat_room, 'messages': messages, 'username': session['username']}
    return render_template('chat/chat.html', **data)


@blueprint.route('/chat/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form.get('title', '')
        if title != '':
            chat_room = ChatRoom(title)
            db.session.add(chat_room)
            db.session.commit()
            return redirect(url_for('controllers.chat', room_id=chat_room.id))
    return render_template('chat/create.html')


@blueprint.route('/chat/delete/<int:message_id>')
def delete(message_id):
    result = {'status': 'success'}
    try:
        db.session.delete(Message.query.get(message_id))
        db.session.commit()
    except UnmappedInstanceError:
        result['status'] = 'fail'
    return jsonify(result)


@blueprint.route('/')
def index():
    chat_rooms = ChatRoom.query.all()
    data = {'chat_rooms': chat_rooms}
    return render_template('chat/index.html', **data)
