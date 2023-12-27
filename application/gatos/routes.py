import math
from datetime import datetime
from flask import render_template, current_app, request
from application import db

from . import gatos

PRODUCTOS_POR_PAGINA = 6
fecha_actual = datetime.now()

def obtener_productos_gatos(page):
    """ obtener los productos relacionados con gatos"""
    try:
        with db.connection.cursor() as cur:
            consulta_sql = "SELECT * FROM producto WHERE fk_category = %s" 
            cur.execute(consulta_sql, (2,))
            productos = cur.fetchall()
            current_app.logger.info(f"{fecha_actual} Consulta SQL ejecutada: {consulta_sql}")
        
        orden = request.args.get('orden', 'nombre_asc')

        if orden == 'nombre_asc':
            productos = sorted(productos, key=lambda x: x[2])  # nombre ascendente
        elif orden == 'nombre_desc':
            productos = sorted(productos, key=lambda x: x[2], reverse=True)  # nombre descendente
        elif orden == 'precio_asc':
            productos = sorted(productos, key=lambda x: x[5])  # precio ascendente
        elif orden == 'precio_desc':
            productos = sorted(productos, key=lambda x: x[5], reverse=True)  # precio descendente
        
        elementos_por_pagina = PRODUCTOS_POR_PAGINA
        total_productos = len(productos)
        total_paginas = int(math.ceil(total_productos / elementos_por_pagina))
        inicio = (page - 1) * elementos_por_pagina
        fin = inicio + elementos_por_pagina
        productos_paginados = productos[inicio:fin]
        return {
            "productos": productos_paginados,
            "total_paginas": total_paginas,
            "pagina_actual": page,
            "elementos_por_pagina": elementos_por_pagina,
            "total_productos": total_productos,
            "orden": orden 
        }
    except Exception as e:
        current_app.logger.error(f"{fecha_actual} Error al obtener productos de gatos: {str(e)}")
        return None

@gatos.route("/gatos")
def gatos_productos():
    """Función para mostrar los productos de gatos"""
    data = {
        "titulo": "Gatos",
    }
    page = request.args.get('page', 1, type=int)
    productos_paginados = obtener_productos_gatos(page)
    if productos_paginados is not None:
        return render_template("gatos/gatos.html", data=data, productos=productos_paginados)
    else:
        return render_template("error/error.html", mensaje="Error al obtener productos de gatos")
    
