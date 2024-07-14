from Interfaz.Inicio import * 

from baseDeDatos.Database import iniciarSesion

# Comienza la aplicacion
Bienvenida()

#Comienza iniciar sesion

nombre_usuario = input("Ingrese su nombre de usuario: ")
contrasena = input("Ingrese su contraseña: ")
usuario = iniciarSesion(nombre_usuario, contrasena) 


