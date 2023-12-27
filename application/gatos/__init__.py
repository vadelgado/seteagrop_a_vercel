from flask import Blueprint

gatos = Blueprint('gatos', __name__, template_folder='templates')

from . import routes
