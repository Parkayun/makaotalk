import os, sys; sys.path.insert(0, os.path.abspath('..'));

from makaotalk import create_app
from makaotalk.models import db


def get_app(db_uri):
    os.environ['DB_URI'] = 'sqlite:///../test.db'

    app = create_app()
    db.app = app
    db.create_all()

    return app
