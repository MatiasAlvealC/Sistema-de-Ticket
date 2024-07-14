from Interfaz.Inicio import * 
from baseDeDatos.Database import Database

# Comienza la aplicacion
Bienvenida()

#Comienza iniciar sesion
nombre_usuario = input("Ingrese su nombre de usuario: ")
contrasena = input("Ingrese su contraseña: ")

# Instancia de la clase Database
db = Database()
usuario = db.iniciarSesion(nombre_usuario, contrasena) 
