from functools import wraps
from random import randint

from flask import session


def set_username_if_not(method):
    """Method decorator that is doing set username when session hasn't username key.
    username is contains `anonymous` string with `random integer(10000 ~ 99999)`.
    """
    @wraps(method)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            session['username'] = 'anonymous%s' % ''.join([str(randint(1, 9)) for _ in range(5)])
        return method(*args, **kwargs)
    return decorated_function