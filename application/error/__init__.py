from flask import Blueprint

error = Blueprint('error', __name__, template_folder='templates')   

from . import routes
