from datetime import datetime
from flask import render_template,redirect,url_for,current_app, flash, abort
import MySQLdb
from .import error 

fecha_actual = datetime.now()

#ERRORES HTTP
@error.app_errorhandler(404)
def page_not_found(errores):
    """Función para control de errores en paginas no encontradas"""
    data = {
        "titulo": "Página no encontrada",
    }
    current_app.logger.error(f'{fecha_actual} : pagina no encontrada {errores}')
    return render_template("error/pagina_no_encontrada.html", data=data)

@error.errorhandler(500)
def internal_server_error(e):
    """Función para control de error 500"""
    data = {
        "titulo": "500",
    }
    current_app.logger.error(f'{fecha_actual} : error interno del servidor {e}')
    return render_template("error/500.html", data=data)

#ERRORES DE VALIDACION DE FORMULARIOS

@error.errorhandler(422)
def handle_unprocessable_entity(err):
    """Función para Manejar errores de validación de formularios"""
    data = {
        "titulo": "Datos no procesables",
    }
    current_app.logger.error(f'{fecha_actual} : error 422 datos no procesables {err}')
    return render_template("error/422.html", data=data)

#ERRORES DE AUTENTICACION

@error.app_errorhandler(401)
def status_401(errores):
    """Función para control de paginas sin acceso"""
    flash("Debe iniciar sesión para acceder a nuestros servicios :)")
    current_app.logger.error(f'{fecha_actual} : pagina sin acceso {errores}')
    return redirect(url_for("login"))

@error.errorhandler(403)
def forbidden_error(err):
    """Función para control de paginas sin acceso"""
    data = {
        "titulo": "Datos no procesables",
    }
    current_app.logger.error(f'{fecha_actual} : error 422 permisos insuficientes {err}')
    return render_template("error/403.html", data=data)

#ERROR EN BASE DE DATOS

@error.app_errorhandler(Exception)
def handle_database_error(error):
    """Función para control de errores en base de datos"""
    if (
        isinstance(error, tuple)
        and len(error) == 2
        and error[0] == 2002
        and "Can't connect to server" in error[1]
    ):
        current_app.logger.error(f'{fecha_actual} : no se pudo conectar al servidor {error}')
        return handle_database_error(MySQLdb.OperationalError(*error))
    mensaje = (
        "Lo sentimos, hay un problema de conexión a la base de datos en este momento."
    )
    detalles_error = str(error)
    data = {
        "titulo": "Error de conexión a la base de datos",
        "mensaje": mensaje,
        "detalles_error": detalles_error,
    }
    current_app.logger.error(f'{fecha_actual} : no se pudo conectar al servidor {error}')
    return render_template("error/error_bd.html", data=data), 500





#RUTAS DE PRUEBA PARA MOSTRAR LOS TIPOS DE ERRORES
@error.route('/error')
def producir_error_500():
    """Levanta una excepción para forzar un error 500"""
    abort(500)

@error.route('/error422')
def producir_error_422():
    """Usa abort para provocar un error 422"""
    abort(422)

@error.route('/error403')
def produce_error_403():
    """Levanta una excepción para forzar un error 403"""
    abort(403)