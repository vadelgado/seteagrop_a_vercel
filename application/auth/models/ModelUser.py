from .entities.User import User


class ModelUser():
    """
    Clase para gestionar la autenticación de usuarios.
    Methods:
        login(db, user): Realiza un intento de inicio de sesión del usuario.
    """
    @classmethod
    def login(cls, db, user):
        """
        Realiza un intento de inicio de sesión del usuario.
        Args:
        db (objeto): Conexión a la base de datos.
        user (User): Objeto de usuario que contiene información de inicio de sesión.
        Returns:
        User: Si la autenticación tiene éxito, devuelve un objeto de usuario con información adicional.
        None: Si la autenticación falla.
        Raises:
        Exception: Si se produce un error durante la autenticación.
        """
        try:
            cursor = db.connection.cursor()
            sql = "SELECT identificacion,correo, password,nombre,apellido,tipo_identificacion FROM usuarios WHERE correo = %s"
            cursor.execute(sql, (user.correo,))
            row = cursor.fetchone()
            if row is not None:
                user = User(row[0], row[1], User.check_password(
                    row[2], user.password), row[3], row[4], row[5], )
                return user
            else:
                return None
        except Exception as ex:
            raise ValueError(f"Ha ocurrido un error {ex}") from ex

    @classmethod
    def get_by_id(cls, db, email):
        """
        Obtiene un usuario por su ID.
        Args:
        db (objeto): Conexión a la base de datos.
        id (int): ID del usuario a buscar.  
        Returns:
        User: Objeto de usuario si se encuentra, None si no se encuentra.  
        Raises:
        Exception: Si se produce un error durante la búsqueda.
        """
        try:
            cursor = db.connection.cursor()
            sql = "SELECT identificacion,correo, password,nombre,apellido,tipo_identificacion FROM usuarios WHERE correo = %s"
            cursor.execute(sql, (email,))
            row = cursor.fetchone()
            if row is not None:
                return User(row[0], row[1], None, row[3], row[4], row[5])
            else:
                return None
        except Exception as ex:
            raise ValueError(f"Ha ocurrido un error {ex}") from ex

    @classmethod
    def Save_User(cls, db, user, password):
        """
        Guarda un usuario en la base de datos.
        argumetos:
        db (objeto): Conexión a la base de datos.
        user (User): Objeto de usuario a guardar.
        password (str): Contraseña del usuario.
        excepciones:
        ValueError: Si se produce un error durante la operación.
        """
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO usuarios (identificacion,correo, password, nombre, apellido, tipo_identificacion) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (user.identificacion,user.correo, password, user.nombre, user.apellido,
                           user.tipo_identificacion ))
            db.connection.commit()
            cursor.close()
        except Exception as ex:
            db.connection.rollback()  # Revertir la transacción en caso de error
            raise ValueError(f"Ha ocurrido un error {ex}") from ex

    @classmethod
    def email_exists(cls, db, email):
        """
        Verifica si un correo ya existe en la base de datos.
        argumentos:
        db (objeto): Conexión a la base de datos.
        email (str): Correo a verificar.
        retorno:
            bool: True si el correo ya existe, False si no.
        """
        try:
            cursor = db.connection.cursor()
            sql = "SELECT COUNT(*) FROM usuarios WHERE correo = %s"
            cursor.execute(sql, (email,))
            count = cursor.fetchone()[0]
            return count > 0
        except Exception as ex:
            raise ValueError(f"Ha ocurrido un error {ex} ") from ex
        finally:
            cursor.close()

    @classmethod
    def identification_exists(cls, db, identification):
        """
        Verifica si una identificación ya existe en la base de datos.
        Argumentos:
            db (objeto): Conexión a la base de datos.
            identification (str): Identificación a verificar.
        Retorno:
            bool: True si la identificación ya existe, False si no.
        """
        try:
            cursor = db.connection.cursor()
            sql = "SELECT COUNT(*) FROM usuarios WHERE identificacion = %s"
            cursor.execute(sql, (identification,))
            count = cursor.fetchone()[0]
            return count > 0
        except Exception as ex:
            raise ValueError(f"Ha ocurrido un error {ex}") from ex
        finally:
            cursor.close()