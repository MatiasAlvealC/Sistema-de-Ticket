"""
    Función encargada de presentar el iniciar seccion
"""

import mysql.connector
from baseDeDatos.Database import Database
from negocio.usuarios.Ejecutivo import Ejecutivo
from negocio.usuarios.JefeDeMesa import JefeDeMesa


# Función para iniciar sesión
def iniciarSesion():
    """db = None
    cursor = None"""
    try:
        # Conexión a la base de datos
        db = Database()

        while True:
            try:
                # Pedir credenciales al usuario
                nombre_usuario = input("Ingrese su nombre de usuario: ")
                contrasena = input("Ingrese su contraseña: ")

                # Consultar en la tabla jefemesa
                cursor = db.cursor
                sql_jefe_mesa = (
                    "SELECT * FROM jefemesa WHERE nombre = %s AND contrasena = %s"
                )
                cursor.execute(sql_jefe_mesa, (nombre_usuario, contrasena))
                jefe_mesa = cursor.fetchone()

                # Consultar en la tabla Ejecutivo
                sql_ejecutivo = "SELECT * FROM Ejecutivo WHERE nombreUsuario = %s AND contraseña = %s"
                cursor.execute(sql_ejecutivo, (nombre_usuario, contrasena))
                ejecutivo = cursor.fetchone()

                # Determinar el perfil del usuario
                if jefe_mesa:
                    usuario = JefeDeMesa(*jefe_mesa)  # Instanciar objeto JefeDeMesa
                    print("Inicio de sesión exitoso como Jefe de Mesa.")
                    return usuario, "jefe_de_mesa"
                elif ejecutivo:
                    usuario = Ejecutivo(*ejecutivo)  # Instanciar objeto Ejecutivo
                    print("Inicio de sesión exitoso como Ejecutivo.")
                    return usuario, "ejecutivo"
                else:
                    print("Credenciales incorrectas. Intente nuevamente.")
            except ValueError:
                print("Entrada no válida. Por favor, intente de nuevo.")
            except mysql.connector.Error as err:
                print(f"Error de MySQL: {err}")
                return None, None

    finally:
        if cursor:
            cursor.close()
        if db:
            db.conexion.close()




