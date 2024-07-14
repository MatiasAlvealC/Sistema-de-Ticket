from baseDeDatos.Database import Database
db = Database()

print("\n1. Crear Ejecutivo")
print("2. Crear Área")
print("3. Crear Tipo de Ticket")
print("4. Crear Criticidad")
print("5. Ver Tickets")
print("0. Cerrar sesión")

# Ingresar una opcion
try :
    opcion = input("Seleccione una opción: ")
    while opcion<0 or opcion>5:
        opcion=float(input("Error, ingrese una opcion valida ="))
except ValueError:
    opcion=float(input("Error, ingrese una opcion ="))
    
    
   
for i in range(cant):
    while True:
        try:
            puntaje=int(input('Puntaje del juego '+str(i+1)+' (10-100)='))
            while puntaje<10 or puntaje>100:
                puntaje=int(input('Error, Puntaje del juego '+str(i+1)+' (10-100)='))
            total+=puntaje
            break
        except ValueError:
            pass
   

if opcion == 0:
    break
elif opcion == 1:
    rut=input("Rut del ejecutivo:")
    area=input("Nombre del área")
    db.crearEjecutivo(rut,nombre,apellido_paterno,apellido_materno,nombre_usuario,contrasena,)
elif opcion == 2:
    d.crearArea()
elif opcion == '5':
    input("Presione Enter para continuar...")  # Pausar para permitir que el usuario vea los resultados
else:
    print("Opción no válida")
    input("Presione Enter para continuar...") 