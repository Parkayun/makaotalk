from flask import render_template

from . import chat_blueprint


@chat_blueprint.route('/')
def index():
    return render_template('chat/index.html')
