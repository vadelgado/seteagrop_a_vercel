from datetime import datetime
from flask import redirect, render_template,request, url_for, current_app
from flask_wtf.csrf import CSRFProtect
from flask_login import current_user,login_required
from application import db
from application.servicios.formulario.form_peluqueria import FormPeluqueria
from application.servicios.formulario.form_veterinaria import FormVeterinaria

from . import servicios

csrf = CSRFProtect()

fecha_actual = datetime.now()

def guardar_servicio_peluqueria(identificacion, nombre_mascota, raza_mascota, edad_mascota, servicio_solicitado, fecha_cita, hora_cita, numero_dueno, observaciones):
    """Función para guardar un servicio de peluquería"""
    with db.connection.cursor() as cur:
        consulta_sql = "INSERT INTO citas_peluqueria (identificacion_dueno, nombre_mascota, raza_mascota, edad_mascota, servicio_solicitado, fecha_cita, hora_cita, numero_dueno, observaciones) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cur.execute(consulta_sql, (identificacion, nombre_mascota, raza_mascota, edad_mascota, servicio_solicitado, fecha_cita, hora_cita, numero_dueno, observaciones))
        db.connection.commit()
        

def guardar_servicio_veterinaria(identificacion_dueno, numero_dueno, nombre_mascota, especie_mascota, raza_mascota, edad_mascota, peso_mascota, sexo_mascota, fecha_cita, hora_cita ,razon_cita):
    """Función para guardar un servicio de atención medica veterinaria"""
    with db.connection.cursor() as cur:
        consulta_sql = "INSERT INTO veterinaria (identificacion_dueno, numero_dueno, nombre_mascota, especie_mascota, raza_mascota, edad_mascota, peso_mascota, sexo_mascota, fecha_cita, hora_cita, razon_cita) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s)"
        cur.execute(consulta_sql, (identificacion_dueno, numero_dueno, nombre_mascota, especie_mascota, raza_mascota, edad_mascota, peso_mascota, sexo_mascota, fecha_cita, hora_cita ,razon_cita))
        db.connection.commit()
        


@servicios.route("/servicios/peluqueria", methods=['GET', 'POST'])
@login_required
def peluqueria():
    """Función para agendar servicio de peluquería"""
    data = {
        "titulo": "Peluqueria",
    }
    form = FormPeluqueria(request.form)
    if form.validate_on_submit():
        identificacion = current_user.identificacion
        nombre_mascota = form.nombre_mascota.data
        raza_mascota = form.raza_mascota.data
        edad_mascota = form.edad_mascota.data
        servicio_solicitado = form.servicio_solicitado.data
        fecha_cita = form.fecha_cita.data
        hora_cita = form.hora_cita.data
        numero_dueno = form.numero_dueno.data
        observaciones = form.observaciones.data
        try:            
             guardar_servicio_peluqueria(identificacion, nombre_mascota, raza_mascota, edad_mascota, servicio_solicitado, fecha_cita, hora_cita, numero_dueno, observaciones)
        except ValueError as e:
            current_app.logger.error(f'{fecha_actual}  Error en guardar servicio peluqueria {e}')
            return render_template("error.html")
        return redirect(url_for('bienvenida.index'))
    else:        
        return render_template("servicios/peluqueria.html", form=form, data=data, nombre_usuario=current_user.nombre)

@servicios.route("/servicios/veterinaria", methods=["GET", "POST"])
@login_required
def veterinaria():
    """Función para agendar servicio de atención medica veterinaria"""
    data = {
        "titulo": "Veterinaria",
    }
    form = FormVeterinaria(request.form)
    if form.validate_on_submit():
        identificacion = current_user.identificacion
        telefono_dueno = form.telefono_dueno.data
        nombre_mascota = form.nombre_mascota.data
        especie_mascota = form.especie_mascota.data
        raza_mascota = form.raza_mascota.data
        edad_mascota = form.edad_mascota.data
        peso_mascota = form.peso_mascota.data
        sexo_mascota = form.sexo_mascota.data
        fecha_cita = form.fecha_cita.data
        razon_cita = form.razon_cita.data
        hora_cita = form.hora_cita.data
        try:
            guardar_servicio_veterinaria(identificacion, telefono_dueno, nombre_mascota, especie_mascota, raza_mascota, edad_mascota, peso_mascota, sexo_mascota, fecha_cita, razon_cita, hora_cita)
        except ValueError as e:
            current_app.logger.error(f'{fecha_actual}  Error en guardar servicio veterinaria {e}')
            return render_template("error.html")
        return redirect(url_for('bienvenida.index'))
    else:
        return render_template("servicios/veterinaria.html", form=form, data=data, nombre_usuario=current_user.nombre, correo_usuario=current_user.correo)