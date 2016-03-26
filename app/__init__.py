from flask import Flask

from .models import db


app = Flask(__name__)


def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'
    db.init_app(app)

    from .views import blueprint
    app.register_blueprint(blueprint)

    return app
