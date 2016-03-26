from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager

from app import create_app, socketio
from app.models import db


app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def setup_db():
    db.create_all()


@manager.command
def run():
    socketio.run(app, debug=True)


if __name__ == "__main__":
    manager.run()
