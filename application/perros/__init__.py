from flask import Blueprint

perros = Blueprint('perros', __name__, template_folder='templates')

from . import routes
