"""
La clase FormPeluqueria contiene campos para el nombre del dueño de la mascota, 
nombre de la mascota, raza de la mascota, edad de la mascota, servicio solicitado,
fecha y hora de la cita, número de contacto del propietario y cualquier 
observación adicional. También incluye validadores personalizados.
"""
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    DateField,
    IntegerField,
    TextAreaField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
    Length,    
)
from application.funciones_personalizadas import (
    validate_date_in_future,
    validate_no_special_characters,
    generar_opciones_hora,
    validate_time_in_future,
)

# Constantes para los campos del formulario
NOMBRE_DUENO = "Nombre del dueño"
NOMBRE_MASCOTA = "Nombre de la mascota"
RAZA_MASCOTA = "Raza de la mascota"
EDAD_MASCOTA = "Edad de la mascota"
SERVICIO_SOLICITADO = "Servicio solicitado"
FECHA_CITA = "Fecha de la cita"
HORA_CITA = "Hora de la cita"
NUMERO_DUENO = "Número de contacto"
OBSERVACIONES = "Observaciones"

class FormPeluqueria(FlaskForm):
    """Formulario para agendar citas de peluquería para mascotas.

    Atributos:
    - nombre_dueno (StringField): campo para ingresar el nombre del dueño de la mascota.
    - nombre_mascota (StringField): campo para ingresar el nombre de la mascota.
    - raza_mascota (StringField): campo para ingresar la raza de la mascota.
    - edad_mascota (IntegerField): campo para ingresar la edad de la mascota.
    - servicio_solicitado (SelectField): campo para seleccionar el servicio solicitado.
    - fecha_cita (DateField): campo para ingresar la fecha de la cita.
    - hora_cita (TimeField): campo para ingresar la hora de la cita.
    - numero_dueno (IntegerField): campo para ingresar el número de contacto del dueño.
    - observaciones (TextAreaField): campo para ingresar observaciones adicionales.
    - submit (SubmitField): botón para enviar el formulario.
    """

    nombre_dueno = StringField(
        NOMBRE_DUENO,
    )
    nombre_mascota = StringField(
        NOMBRE_MASCOTA,
        validators=[
            DataRequired("El nombre de la mascota es obligatorio. !"),
            validate_no_special_characters,
        ],
    )
    raza_mascota = StringField(
        RAZA_MASCOTA,
    )
    edad_mascota = StringField(
        EDAD_MASCOTA,
        validators=[
            DataRequired("La edad de la mascota es obligatoria."),
        ],
    )
    servicio_solicitado = SelectField(
        SERVICIO_SOLICITADO,
        choices=[
            ("", "Seleccione"),
            ("Limpieza e higiene", "Limpieza e higiene"),
            ("Spa", "Spa para mascota"),
            ("corte de pelo", "Corte de pelo"),
            ("corte de uñas", "Corte de uñas"),
        ],
        validators=[DataRequired("El servicio solicitado es obligatorio. !")],
    )
    fecha_cita = DateField(
        FECHA_CITA,
        validators=[
            DataRequired("La fecha de la cita es obligatoria. !"),
            validate_date_in_future,
        ],
    )
    hora_cita = SelectField(
        HORA_CITA,
        choices=generar_opciones_hora(),
        validators=[DataRequired("La hora es obligatoria. !"),
        validate_time_in_future
        ],
    )
    numero_dueno = IntegerField(
        NUMERO_DUENO,
        validators=[
            DataRequired("El número de contacto es obligatorio. !"),
        ],
    )
    observaciones = TextAreaField(
        OBSERVACIONES,
        validators=[
            DataRequired("Las observaciones son obligatoria. !"),
            Length(
                max=500,
                message="Las observaciones no debe exceder los 500 caracteres.",
            ),
        ],
    )
    submit = SubmitField("Agendar")
