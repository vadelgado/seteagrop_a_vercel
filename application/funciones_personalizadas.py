# Validadores personalizados
from datetime import date, datetime, timedelta
from wtforms import ValidationError

def validate_date_in_future(_, field):
    """
    Valida que la fecha proporcionada no sea anterior a la fecha actual.
    Si la fecha es anterior a la fecha actual, se lanza una excepción de validación.
    """
    if field.data < date.today():
        raise ValidationError(
            "La fecha de la cita no puede ser anterior al dia de hoy!."
        )


def validate_no_special_characters(_, field):
    """
    Valida que el campo proporcionado no contenga números ni caracteres especiales.
    Si el campo contiene números o caracteres especiales, se lanza una excepción de validación.
    """
    if not field.data.replace(" ", "").isalpha():
        raise ValidationError("Este campo solo debe contener letras y espacios.")


def generar_opciones_hora():
    """ lista de 30 minutos entre las 08:00 A.M. y las 08:00 P.M.

    Returns:
        list: Una lista de tuplas con opciones de tiempo en el formato (HH:MM AM/PM, HH:MM AM/PM).
              La primera tupla es ("", "Seleccione").
    """
    hora_inicio = datetime.strptime("08:00 AM", "%I:%M %p")
    hora_fin = datetime.strptime("08:00 PM", "%I:%M %p")
    intervalo = timedelta(minutes=30)
    opciones_hora = []

    while hora_inicio <= hora_fin:
        opciones_hora.append(
            (hora_inicio.strftime("%I:%M %p"), hora_inicio.strftime("%I:%M %p"))
        )
        hora_inicio += intervalo

    return [("", "Seleccione")] + opciones_hora


def validate_time_in_future(form, _):
    """
    Valida que la hora proporcionada no sea anterior a la hora actual.
    ni a la fecha actual.
    """
    hora_ingresada = form.hora_cita.data
    hora_formateada = datetime.strptime(hora_ingresada, "%I:%M %p").time()
    if (
        form.fecha_cita.data == date.today()
        and hora_formateada < datetime.now().time()
    ):
        raise ValidationError(
            "La hora de la cita no puede ser anterior a la hora actual si la fecha es de hoy 😔."
        )