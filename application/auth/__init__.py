from flask import Blueprint
from application import create_app

auth = Blueprint('auth', __name__, template_folder='templates')

from . import routes 