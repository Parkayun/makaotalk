from flask import Blueprint

blueprint = Blueprint('controllers', __name__)

from . import web
from . import websocket
