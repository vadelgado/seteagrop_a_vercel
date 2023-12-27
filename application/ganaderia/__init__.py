from flask import Blueprint

ganaderia = Blueprint('ganaderia', __name__, template_folder='templates')

from . import routes
