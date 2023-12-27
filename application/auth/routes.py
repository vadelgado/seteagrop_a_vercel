
import logging

from datetime import datetime
from flask import render_template, request, flash, redirect, url_for,current_app, session
from flask_login import  login_user, logout_user, login_required
#from werkzeug.urls import url_parse

# # Models
from application.auth.models.ModelUser import ModelUser

# # Entities
from application.auth.models.entities.User import User
from application.auth.formulario.formularios import RegistrationForm, LoginForm
from application import login_manager_app

from . import auth

fecha_actual = datetime.now()

logger = logging.getLogger(__name__)

@login_manager_app.user_loader
def load_user(email):
    """
    Carga un usuario a partir de su dirección de correo electrónico.
    """
    with current_app.app_context():
        db_instance = current_app.config['db']
    return ModelUser.get_by_id(db_instance, email)

# AUTENTICACION

@auth.route("/auth/login", methods=["GET", "POST"])
def login():
    """
    Función para inicio de sesión.
    Esta función maneja las solicitudes GET y POST para la página de inicio de sesión.
    Si se recibe una solicitud POST, verifica las credenciales del usuario y realiza el inicio de sesión si son válidas.
    Args:
        None
    Returns:
        render_template: Renderiza la plantilla de inicio de sesión.
    """
    with current_app.app_context():
        db_instance = current_app.config['db']
    data = {
        "titulo": "Ingresa a tu cuenta",
    }
    form = LoginForm(request.form)
    try:
        if form.validate_on_submit():
            email = request.form["email"]
            user = User(1, request.form["email"], request.form["password"])
            logged_user = ModelUser.login(db_instance, user)
            if logged_user is not None:
                if logged_user.password:
                    login_user(logged_user)
                    next_page = request.form.get('next')
                    print(next_page)
                    if next_page == 'None':
                        next_page = url_for('auth.logged')
                    return redirect(next_page)
                else:
                    flash("Usuario o contraseña incorrectos")
                    current_app.logger.error(f'{fecha_actual}: Usuario contraseña incorrecta {email}')
                    return render_template("auth/login.html", data=data, form=form)
            else:
                flash("Usuario no encontrado")
                current_app.logger.error(f'{fecha_actual}: Usuario no encontrado {email}')
                return render_template("auth/login.html", data=data, form=form)
        else:
            return render_template("auth/login.html", data=data, form=form)
    except ImportError as ex:
        flash("Ha ocurrido un error")
        current_app.logger.error(f'{fecha_actual} Error en el login: {ex}')
        return render_template("auth/login.html", data=data, form=form)


@auth.route("/auth/account", methods=["GET", "POST"])
def account():
    """
    Función para registro de usuarios.
    Esta función maneja el registro de usuarios. Si la solicitud es un POST y el formulario
    es válido, se intenta guardar el usuario en la base de datos. Si se produce un error al
    guardar en la base de datos, se muestra un mensaje de error al usuario.
    Args:
        None
    Returns:
        render_template: Renderiza la plantilla de registro de usuarios.
    """
    with current_app.app_context():
        db_instance = current_app.config['db']
    data = {
        "titulo": " Crea tu cuenta",
    }
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        identificacion = form.identificacion.data
        nombre = form.nombre.data
        apellido = form.apellido.data
        tipo_identificacion = form.tipo_identificacion.data
        correo = form.correo.data
        password = form.password.data

        # Validar si el correo existe
        if ModelUser.email_exists(db_instance, correo):
            flash("El correo ya está registrado. Por favor, utiliza otro correo.")
            return render_template("auth/account.html", form=form, data=data)
        
        # Validar si la cedula o identificación existe
        if ModelUser.identification_exists(db_instance, identificacion):
            flash("La identificación ya está registrada. Por favor, utiliza otra identificación.")
            return render_template("auth/account.html", form=form, data=data)

        try:
            user = User(
                identificacion, correo, password, nombre, apellido, tipo_identificacion
            )
            password = user.set_password(password)
            ModelUser.Save_User(db_instance, user, password)
            #inicia sesión despues del registro
            login_user(user)
            return redirect(url_for("auth.logged"))
        
        except ImportError as ex:
            flash("Error al guardar en la base de datos: ")
            current_app.logger.error(f'{fecha_actual}  Error en el registro de usuario {ex}')
            return render_template("auth/account.html", form=form, data=data)
    else:
        return render_template("auth/account.html", form=form, data=data)


@auth.route("/auth/logged")
@login_required
def logged():
    """Función para retornar la vista del usuario logueado"""
    data = {
        "titulo": "Bienvenid@",
    }
    return render_template("auth/logged.html", data=data)


@auth.route("/logout")
def logout():
    """Función para registro de usuarios."""
    session.clear()
    logout_user()
    return redirect(url_for("auth.login"))