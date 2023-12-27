"""
Este módulo define el formulario para la veterinaria.
Incluye campos para el nombre del dueño, teléfono, correo electrónico,
nombre de la mascota, especie, raza, edad, peso, fecha de la cita, hora de la cita, razon cita.
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
    Email,
    Length,
    NumberRange,
)
from application.funciones_personalizadas import (
    validate_date_in_future,
    validate_no_special_characters,
    generar_opciones_hora,
    validate_time_in_future,
)

# Constantes para los campos del formulario
NOMBRE_DUENO = "Nombre del dueño"
TELEFONO_DUENO = "Teléfono del dueño"
CORREO_DUENO = "Correo electrónico"
NOMBRE_MASCOTA = "Nombre de la mascota"
ESPECIE_MASCOTA = "Especie de la mascota"
RAZA_MASCOTA = "Raza de la mascota"
EDAD_MASCOTA = "Edad de la mascota"
PESO_MASCOTA = "Peso de la mascota"
SEXO_MASCOTA = "Sexo de la mascota"
FECHA_CITA = "Fecha de la cita"
HORA_CITA = "Hora de la cita"
RAZON_CITA = "Razón de la cita"


class FormVeterinaria(FlaskForm):
    """
    Formulario base que incluye los campos comunes para los formularios de la aplicación.
    Los campos incluyen el nombre del dueño, teléfono del dueño, y validaciones para estos campos.
    """

    nombre_dueno = StringField(
        NOMBRE_DUENO,
    )
    telefono_dueno = StringField(
        TELEFONO_DUENO,
        validators=[
            DataRequired("El teléfono del dueño es obligatorio."),
            Length(max=10, message="El teléfono debe tener máximo 10 caracteres."),
        ],
    )
    correo_dueno = StringField(
        CORREO_DUENO,
    )
    nombre_mascota = StringField(
        NOMBRE_MASCOTA,
        validators=[
            DataRequired("El nombre de la mascota es obligatorio."),
            validate_no_special_characters,
        ],
    )
    especie_mascota = SelectField(
        ESPECIE_MASCOTA,
        choices=[
            ("", "Seleccione"),
            ("perro", "Perro"),
            ("gato", "Gato"),
            ("conejo", "Conejo"),
            ("hamster", "Hamster"),
            ("otro", "Otro"),
        ],
        coerce=str,
        validators=[DataRequired("La especie de la mascota es obligatoria.")],
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
    peso_mascota = StringField(
        PESO_MASCOTA,
        validators=[
            DataRequired("El peso de la mascota es obligatorio."),
        ],
    )
    sexo_mascota = SelectField(
        SEXO_MASCOTA,
        choices=[("", "Seleccione"), ("macho", "Macho"), ("hembra", "Hembra")],
        validators=[DataRequired("El sexo de la mascota es obligatorio.")],
    )
    fecha_cita = DateField(
        FECHA_CITA,
        format="%Y-%m-%d",
        validators=[
            DataRequired("La fecha de la cita es obligatoria."),
            validate_date_in_future,
        ],
    )
    hora_cita = SelectField(
        HORA_CITA,
        choices=generar_opciones_hora(),
        validators=[DataRequired("La hora es obligatoria. !"), validate_time_in_future],
    )
    razon_cita = TextAreaField(
        RAZON_CITA,
        validators=[
            DataRequired("La razón de la cita es obligatoria."),
            Length(
                max=500,
                message="La razón de la cita no debe exceder los 500 caracteres.",
            ),
        ],
    )
    submit = SubmitField("Enviar")
