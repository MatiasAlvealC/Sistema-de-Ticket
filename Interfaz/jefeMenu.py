from baseDeDatos.Database import Database
db = Database()


def jefeMenu():
    while True:

        print("\n1. Crear Ejecutivo")
        print("2. Crear Área")
        print("3. Crear Tipo de Ticket")
        print("4. Crear Criticidad")
        print("5. Ver Tickets")
        print("0. Cerrar sesión")

    # Ingresar una opcion
        try :
            opcion = float(input("Seleccione una opción: "))
            while opcion < 0 or opcion > 5:
                opcion=float(input("Error, ingrese una opcion valida ="))
        except ValueError:
            opcion=float(input("Error, ingrese una opcion ="))
            
            
        
        """for i in range(cant):
            while True:
                try:
                    puntaje=int(input('Puntaje del juego '+str(i+1)+' (10-100)='))
                    while puntaje<10 or puntaje>100:
                        puntaje=int(input('Error, Puntaje del juego '+str(i+1)+' (10-100)='))
                    total+=puntaje
                    break
                except ValueError:
                    pass
        """


        # Manejo de opciones

        if opcion == 0:
            break
        elif opcion == 1:
            while True:
                try:
                    rutEjecutivo = input("Rut del ejecutivo: ")
                    rutJefeMesa = input("Rut del Jefe de Mesa: ")
                    idArea = input('Id Area: ')
                    nombre = input("Nombre del ejecutivo: ")
                    apellido_paterno = input("Apellido paterno del ejecutivo: ")
                    apellido_materno = input("Apellido materno del ejecutivo: ")
                    nombre_usuario = input("Nombre de usuario del ejecutivo: ")
                    contrasena = input("Contraseña del ejecutivo: ")
                    estado = "Activo"  # Estado predeterminado
                    db.crearEjecutivo(rutEjecutivo, rutJefeMesa, idArea, estado, nombre, apellido_paterno, 
                                    apellido_materno, nombre_usuario, contrasena)
                    break
                except ValueError:
                    print("Error, ingrese datos válidos.")
        elif opcion == 2:
            while True:
                try:
                    idArea = input("ID del área: ")
                    rutJefeMesa = input("Rut del Jefe de Mesa: ")
                    nombre_area = input("Nombre del área: ")
                    descripcion = input("Descripción del área: ")
                    db.crearArea(idArea, rutJefeMesa, nombre_area, descripcion)
                    break
                except ValueError:
                    print("Error, ingrese datos válidos.")
        elif opcion == 3:
            while True:
                try:
                    idTipoTicket = input("ID del tipo de ticket: ")
                    rutJefeMesa = input("Rut del Jefe de Mesa: ")
                    nombre_tipo = input("Nombre del tipo de ticket: ")
                    descripcion = input("Descripción del tipo de ticket: ")
                    db.crearTipoTicket(idTipoTicket, rutJefeMesa, nombre_tipo, descripcion)
                    break
                except ValueError:
                    print("Error, ingrese datos válidos.")
        elif opcion == 4:
            while True:
                try:
                    idCriticidad = input("ID de la criticidad: ")
                    rutJefeMesa = input("Rut del Jefe de Mesa: ")
                    nombre_criticidad = input("Nombre de la criticidad: ")
                    descripcion = input("Descripción de la criticidad: ")
                    db.crearCriticidad(idCriticidad, rutJefeMesa, nombre_criticidad, descripcion)
                    break
                except ValueError:
                    print("Error, ingrese datos válidos.")
        elif opcion == 5:
            while True:
                try:
                    input("Presione Enter para continuar...")  # Pausar para permitir que el usuario vea los resultados
                    db.ver_ticket()
                except ValueError:
                    print("Error, intente nuevamente.")
        else:
            print("Opción no válida")
            input("Presione Enter para continuar...")
