from flask import Flask


app = Flask(__name__)


def create_app():
    from .views import blueprint
    app.register_blueprint(blueprint)

    return app
