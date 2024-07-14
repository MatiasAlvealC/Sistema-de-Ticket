from presentacion.Inicio import * 

from presentacion.IniciarSesion import iniciarSesion
from negocio.usuarios.Ejecutivo import Ejecutivo
from negocio.usuarios.JefeDeMesa import JefeDeMesa

# Comienza la aplicacion
Bienvenida()

#Comienza iniciar sesion

nombre_usuario = input("Ingrese su nombre de usuario: ")
contrasena = input("Ingrese su contraseña: ")
usuario = iniciarSesion()


