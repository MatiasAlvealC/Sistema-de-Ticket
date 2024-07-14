from Interfaz.Inicio import * 
from baseDeDatos.Database import Database

# Comienza la aplicacion
Bienvenida()

#Comienza iniciar sesion
nombre_usuario = input("Ingrese su nombre de usuario: ")
contrasena = input("Ingrese su contraseña: ")

# Instancia de la clase Database
db = Database()
usuario,perfil = db.iniciarSesion(nombre_usuario, contrasena) 

if perfil == "jefe":
    usuario.menu()
elif perfil == "ejecutivo":
    # Aquí puedes agregar las acciones para el ejecutivo
    print("Acciones para el ejecutivo aún no implementadas")
    pass