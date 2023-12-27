from flask import render_template
from . import nosotros

@nosotros.route("/nosotros")
def nosotros():
    """Función para mostrar infomacion acerca de la empresa"""
    data = {
        "titulo": "Nosotros",
    }
    return render_template("nosotros/nosotros.html", data=data)
