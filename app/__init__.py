from flask import Flask


app = Flask(__name__)


def create_app():
    from .chat import chat_blueprint
    app.register_blueprint(chat_blueprint)

    return app
