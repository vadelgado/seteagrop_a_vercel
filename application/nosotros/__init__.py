from flask import Blueprint

nosotros = Blueprint('nosotros', __name__, template_folder='templates')

from . import routes
 