import os
from flask import Flask
from flask_socketio import SocketIO

from .models import db


app = Flask(__name__)
socketio = SocketIO(app)


def create_app():
    app.config['SECRET_KEY'] = 'asdf'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)

    from .controllers import blueprint
    app.register_blueprint(blueprint)

    return app
