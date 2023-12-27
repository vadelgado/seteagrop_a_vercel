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
CANTIDAD = "Quantytie"



class FormCarrito(FlaskForm):
    """
    Formulario base que incluye los campos comunes para los formularios de la aplicación.
    Los campos incluyen el nombre del dueño, teléfono del dueño, y validaciones para estos campos.
    """

    cantidad = IntegerField(
        CANTIDAD,
        validators=[
            DataRequired("La Cantidad de Articulos es requerida. !"),
        ],
    )