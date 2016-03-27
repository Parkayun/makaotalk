from flask import render_template, request, redirect, session, url_for

from . import blueprint
from ..models import db
from ..utils.decorators import set_username_if_not
from ..models.chat import ChatRoom, Message


@blueprint.route('/chat/create/', methods=('GET', 'POST'))
def web_chat_create():
    """Page of creating chat room.
    To create chat room by POST method with `title` form value.
    """
    if request.method == 'POST':
        title = request.form.get('title', '')
        if title != '':
            chat_room = ChatRoom(title)
            db.session.add(chat_room)
            db.session.commit()
            return redirect(url_for('controllers.web_chat_room', room_id=chat_room.id))
    return render_template('chat/create.html')


@blueprint.route('/chat/<int:room_id>/')
@set_username_if_not
def web_chat_room(room_id):
    """Page of real-time chat room.
    This page shows previous chat log and can real-time chat.
    And this controller doing set username if not exists by set_username_if_not decorator.

    :param room_id: primary key of :class:`~makaotalk.models.chat.ChatRoom`
    :type room_id: :class:`int`
    """
    chat_room = ChatRoom.query.get_or_404(room_id)
    messages = Message.query.filter_by(chat_room=chat_room)
    data = {'chat_room': chat_room, 'messages': messages, 'username': session['username']}
    return render_template('chat/chat.html', **data)


@blueprint.route('/')
def web_index():
    """Page of index.
    This page lists up chat rooms.
    """
    chat_rooms = ChatRoom.query.all()
    data = {'chat_rooms': chat_rooms}
    return render_template('chat/index.html', **data)
