from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .chat import ChatRoom
