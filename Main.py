from presentacion.Inicio import * 

from presentacion.IniciarSesion import iniciarSesion
from negocio.usuarios.Ejecutivo import Ejecutivo
from negocio.usuarios.JefeDeMesa import JefeDeMesa

# Comienza la aplicacion
Bienvenida()

#Comienza iniciar sesion

usuario, perfil = iniciarSesion()

if usuario and perfil:
    if perfil == "jefe_de_mesa":
        usuario.menu()
    elif perfil == "ejecutivo":
        # Aquí puedes agregar las acciones para el ejecutivo
        print("Acciones para el ejecutivo aún no implementadas")
        pass

