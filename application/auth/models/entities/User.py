""" Esta función es parte del sistema de hashing y verificación de contraseñas en Flask y 
se utiliza comúnmente para implementar la autenticación de usuarios de forma segura."""
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


class User(UserMixin):  # hereda de usermixin para implementar metodos como isauthenticated, get_id
    """
    Clase para representar a un usuario.
    Attributes:
        identificacion (int): El identificador único del usuario.
        email (str): La dirección de correo electrónico del usuario.
        password (str): La contraseña del usuario almacenada de forma segura.
        fullname (str): El nombre completo del usuario (opcional).
    """

    def __init__(self, identificacion, correo, password, nombre="", apellido="", tipo_identificacion="") -> None:
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido
        self.tipo_identificacion = tipo_identificacion
        self.correo = correo
        self.password = password

    # decorador para no tener que instanciar la clase
    # es un método de clase en lugar de un método de instancia
    @classmethod
    def check_password(cls, hashed_password, password):
        """
        Verifica si una contraseña coincide con su hash almacenado.
        Args:
            hashed_password (str): El hash de la contraseña almacenada.
            password (str): La contraseña introducida por el usuario para verificar.
        Returns:
            bool: True si la contraseña coincide, False si no.
        """
        return check_password_hash(hashed_password, password)
    
    def get_id(self):
        return self.correo
    
    def set_password(self, password):
        """
        Hashea la contraseña antes de almacenarla en la base de datos.
        Args:
            password (str): Contraseña en texto claro.
        Returns:
            str: Contraseña hasheada.
        """
        return generate_password_hash(password)
    

#print(generate_password_hash("angela1234"))
