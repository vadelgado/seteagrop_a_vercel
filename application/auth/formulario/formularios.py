""" Validacion de formularios login y registro con wtf
."""
import re
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, HiddenField
from wtforms.validators import DataRequired, Email, EqualTo, Length,ValidationError


class RegistrationForm(FlaskForm):
    """ Esta """
    nombre = StringField('Nombre', validators=[
    DataRequired("El nombre es obligatorio")], render_kw={"autocomplete": "off"})
    apellido = StringField('Apellido', validators=[
    DataRequired("El apellido es obligatorio")], render_kw={"autocomplete": "off"})
    identificacion = StringField(
    'Número de Identificación', validators=[DataRequired("El número de identificación es obligatorio")],
    render_kw={"autocomplete": "off"})
    tipo_identificacion = SelectField('Tipo de Identificación',
    choices=[ ('cedula ciudadania','Cédula de ciudadania'),
    ('cedula extranjeria','Cédula de extranjería'),
    ('nit', 'NIT'),
    ('tarjeta de identidad','Tarjeta de Identidad'),
    ('tarjeta de extranjeria', 'Tarjeta de Extranjeria'),
    ('Pasaporte', 'Pasaporte'),
    ('documento de identificación extranjero', 'Documento de identificación Extranjero')],
    validators=[DataRequired()])
    correo = StringField('Correo', validators=[DataRequired(
    "El correo es obligatorio"), Email("El email es inválido")], render_kw={"autocomplete": "off"})
    password = PasswordField('Contraseña', validators=[DataRequired("La contraseña es obligatoria"), Length(
    min=8, message="La contraseña debe tener al menos 8 caracteres."), EqualTo('confirmPassword', message='Las contraseñas deben coincidir')])
    confirmPassword = PasswordField(
    'Confirmar Contraseña', validators=[DataRequired("Confirme la contraseña")])
   
    def validate_password(self, password):
        """  validación de contraseña """
        if not any(char.isupper() for char in password.data):
            raise ValidationError('La contraseña debe contener al menos una letra mayúscula.')

        if not any(char.islower() or char.isdigit() for char in password.data):
            raise ValidationError('La contraseña debe contener al menos una letra minúscula o un número.')

        if not any(char in "!@#$%^&*()-_=+{}[]|;:'<>,.?/" for char in password.data):
            raise ValidationError('La contraseña debe contener al menos un caracter especial.')
        
    def validate_identificacion(self, identificacion):
        """Valida que en el campo de identificación solo se ingresen números."""
        if not re.match("^[0-9]+$", identificacion.data):
            raise ValidationError('La identificación debe contener solo números.')


class LoginForm(FlaskForm):
    """  validacion para el login """
    email = StringField('Correo', validators=[DataRequired(
        "Campo obligatorio"), Email("El email es inválido")], render_kw={"autocomplete": "off"})
    password = PasswordField('Contraseña', validators=[
                             DataRequired("Campo obligatorio")], render_kw={"autocomplete": "off"})
    next = HiddenField()

