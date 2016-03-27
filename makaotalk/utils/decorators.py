from functools import wraps
from random import randint

from flask import session


def set_username_if_not(method):
    @wraps(method)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            session['username'] = 'anonymous%s' % ''.join([str(randint(1, 9)) for _ in range(5)])
        return method(*args, **kwargs)
    return decorated_function