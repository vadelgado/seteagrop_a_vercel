import os
from flask import send_from_directory

from . import main

@main.route("/favicon.ico")
def favicon():
    """Función que devuelve un icono"""
    favicon_path = os.path.join(main.root_path, "static")
    return send_from_directory(favicon_path, "favicon.ico", mimetype="image/x-icon")
