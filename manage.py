from flask.ext.script import Manager

from app import create_app


app = create_app()
manager = Manager(app)


@manager.command
def setup_db():
    from app.models import db
    db.create_all()


@manager.command
def run():
    app.run()


if __name__ == "__main__":
    manager.run()
