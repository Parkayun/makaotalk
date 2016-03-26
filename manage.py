from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager

from app import create_app
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
    app.run(debug=True)


if __name__ == "__main__":
    manager.run()
