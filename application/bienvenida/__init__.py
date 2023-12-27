from flask import Blueprint

bienvenida = Blueprint('bienvenida', __name__, template_folder='templates')

from . import routes 