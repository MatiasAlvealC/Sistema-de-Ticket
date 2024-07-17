from Interfaz.Inicio import * 
from baseDeDatos.Database import Database
from Interfaz.jefeMenu import *
from Interfaz.ejecutivoMenu import *
from Interfaz.limpiarPantalla import *
db = Database()


while True:
    limpiar_pantalla()  # Limpia la pantalla antes de comenzar
    # Comienza la aplicacion
    Bienvenida()

    #Comienza iniciar sesion

    # Instancia de la clase Database
    usuario,perfil = db.iniciarSesion() #nombre_usuario, contrasena) 

    limpiar_pantalla()  # Limpia la pantalla 
    if perfil == "jefe":
        jefeMenu(usuario)
    elif perfil == "ejecutivo":
        ejecutivoMenu(usuario)
