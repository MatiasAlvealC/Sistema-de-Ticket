from baseDeDatos.Database import *

db = Database()



# Funcion principal del menu ejecutivo
def jefeMenu():
    while True:

        print("\n1. Gestionar Ejecutivos")
        print("2. Gestionar Área")
        print("3. Gestionar Tipo de Ticket")
        print("4. Gestionar Criticidad")
        print("5. Ver Tickets")
        print("0. Cerrar sesión")

    # Ingresar una opcion
        try :
            opcion = int(input("Seleccione una opción: "))
            while opcion < 0 or opcion > 5:
                opcion=int(input("Error, ingrese una opcion valida ="))
        except ValueError:
            opcion=int(input("Error, ingrese una opcion ="))


        # Manejo de opciones

        if opcion == 0:
            break
        elif opcion == 1:
            while True:
                try:
                    # se llama a la funcion adminsitrar ejecutivo, la que tiene el menu para administrar ejecutivos
                    gestionarEjecutivo()
                    break
                except ValueError:
                    print("Error, ingrese datos válidos.")
        elif opcion == 2:
            while True:
                try:
                    gestionarArea()
                    break
                except ValueError:
                    print("Error, ingrese datos válidos.")
        elif opcion == 3:
            while True:
                try:
                    gestionarTipoTicket()
                    break
                except ValueError:
                    print("Error, ingrese datos válidos.")
        elif opcion == 4:
            while True:
                try:
                    gestionarCriticidad()
                    break
                except ValueError:
                    print("Error, ingrese datos válidos.")
        elif opcion == 5:
            while True:
                try:
                    ver_menu_filtro()
                except ValueError:
                    print("Error, intente nuevamente.")
        else:
            print("Opción no válida")
            input("Presione Enter para continuar...")


# Función gestionar ejecutivos

def gestionarEjecutivo():
    while True:

        print("\n1. Ver Ejecutivos")
        print("2. crear Ejecutivos")
        print("3. Eliminar Ejecutivos")
        print("0. Volver al menu anterior")

        try :
            opcion = int(input("Seleccione una opción: "))
            while opcion < 0 or opcion > 3:
                opcion=int(input("Error, ingrese una opcion valida ="))
        except ValueError:
            opcion=int(input("Error, ingrese una opcion ="))

        if opcion == 0:
            break
        elif opcion == 1:
            db.mostrarEjectuvos()
        elif opcion == 2:   
            rutEjecutivo = input("Rut del ejecutivo: ")
            rutJefeMesa = input("Rut del Jefe de Mesa: ")
            idArea = input('Id Area: ')
            nombre = input("Nombre del ejecutivo: ")
            apellido_paterno = input("Apellido paterno del ejecutivo: ")
            apellido_materno = input("Apellido materno del ejecutivo: ")
            nombre_usuario = input("Nombre de usuario del ejecutivo: ")
            contrasena = input("Contraseña del ejecutivo: ")
            estado = "Activo"  # Estado predeterminado
            db.crearEjecutivo(rutEjecutivo, rutJefeMesa, idArea, estado, nombre, apellido_paterno, apellido_materno, nombre_usuario, contrasena)
        elif opcion == 3:
            rutEjecutivo = input("Rut del ejecutivo a eliminar: ")
            db.EliminarEjecutivo(rutEjecutivo)
        else:
            print("Opción no válida")
            input("Presione Enter para continuar...")

# Función Gestionar Area

def gestionarArea():
    while True:

        print("\n1. Ver Areas")
        print("2. crear Area")
        print("3. Actualizar Area")
        print("4. Eliminar Area")
        print("0. Volver al menu anterior")

        try :
            opcion = int(input("Seleccione una opción: "))
            while opcion < 0 or opcion > 4:
                opcion=int(input("Error, ingrese una opcion valida ="))
        except ValueError:
            opcion=int(input("Error, ingrese una opcion ="))

        if opcion == 0:
            break
        elif opcion == 1:
            db.mostrarAreas()
        elif opcion == 2:
            idArea = input("ID del área: ")
            rutJefeMesa = input("Rut del Jefe de Mesa: ")
            nombre_area = input("Nombre del área: ")
            descripcion = input("Descripción del área: ")
            db.crearArea(idArea, rutJefeMesa, nombre_area, descripcion)
        elif opcion == 3:
            idArea = input("ID del área a editar: ")
            while True:
                print("¿Que desea cambiar?")
                print("1. Nombre")
                print("2. Descripcion")
                print("0. No cambiar nada")
                try :
                    opcion = int(input("Seleccione una opción: "))
                    while opcion < 0 or opcion > 2:
                        opcion=int(input("Error, ingrese una opcion valida ="))
                except ValueError:
                    opcion=int(input("Error, ingrese una opcion ="))
                if opcion == 0:
                    break
                elif opcion == 1:
                    nuevoElemento = input("Nuevo nombre: ")
                    param = "nombre"
                elif opcion == 2:
                    nuevoElemento = input("Nueva descripcion: ")
                    param = "descripcion"
                else:
                    print("Opción no válida")
                    input("Presione Enter para continuar...")
                db.editarArea(idArea,param,nuevoElemento)
                break
        elif opcion == 4:
            idArea = input("Id del area a eliminar: ")
            db.eliminarAreaPorId(idArea)
        else:
            print("Opción no válida")
            input("Presione Enter para continuar...")



# Función Gestionar tipode ticket

def gestionarTipoTicket():
    while True:

        print("\n1. Ver Tipo de tickets")
        print("2. crear tipo de ticket")
        print("3. Actualizar tipo de ticket")
        print("4. Eliminar tipo de ticket")
        print("0. Volver al menu anterior")

        try :
            opcion = int(input("Seleccione una opción: "))
            while opcion < 0 or opcion > 4:
                opcion=int(input("Error, ingrese una opcion valida ="))
        except ValueError:
            opcion=int(input("Error, ingrese una opcion ="))

        if opcion == 0:
            break
        elif opcion == 1:
            db.mostrarTipoTicketes()
        elif opcion == 2:
            idTipoTicket = input("ID del tipo de ticket: ")
            rutJefeMesa = input("Rut del Jefe de Mesa: ")
            nombre_tipoTicket = input("Nombre del tipo de ticket: ")
            descripcion = input("Descripción del tipo de ticket: ")
            db.crearTipoTicket(idTipoTicket, rutJefeMesa, nombre_tipoTicket, descripcion)
        elif opcion == 3:
            idTipoTicket = input("ID del tipo de ticket a editar: ")
            while True:
                print("¿Que desea cambiar?")
                print("1. Nombre")
                print("2. Descripcion")
                print("0. No cambiar nada")
                try :
                    opcion = int(input("Seleccione una opción: "))
                    while opcion < 0 or opcion > 2:
                        opcion=int(input("Error, ingrese una opcion valida ="))
                except ValueError:
                    opcion=int(input("Error, ingrese una opcion ="))
                if opcion == 0:
                    break
                elif opcion == 1:
                    nuevoElemento = input("Nuevo nombre: ")
                    param = "nombre"
                elif opcion == 2:
                    nuevoElemento = input("Nueva descripcion: ")
                    param = "descripcion"
                else:
                    print("Opción no válida")
                    input("Presione Enter para continuar...")
                db.editarTipoTicket(idTipoTicket,param,nuevoElemento)
                break
        elif opcion == 4:
            idArea = input("Id del tipo de ticket a eliminar: ")
            db.eliminarTipoDeTicketPorId(idTipoTicket)
        else:
            print("Opción no válida")
            input("Presione Enter para continuar...")



# Función Gestionar Criticidad

def gestionarCriticidad():
    while True:

        print("\n1. Ver criticidades")
        print("2. crear criticidad")
        print("3. Actualizar criticidad")
        print("4. Eliminar criticidad")
        print("0. Volver al menu anterior")

        try :
            opcion = int(input("Seleccione una opción: "))
            while opcion < 0 or opcion > 4:
                opcion=int(input("Error, ingrese una opcion valida ="))
        except ValueError:
            opcion=int(input("Error, ingrese una opcion ="))

        if opcion == 0:
            break
        elif opcion == 1:
            db.mostrarCriticidades()
        elif opcion == 2:
            idCriticidad = input("ID del criticidad: ")
            rutJefeMesa = input("Rut del Jefe de Mesa: ")
            nombre_criticidad = input("Nombre del criticidad: ")
            descripcion = input("Descripción del criticidad: ")
            db.crearCriticidad(idCriticidad, rutJefeMesa, nombre_criticidad, descripcion)
        elif opcion == 3:
            idCriticidad = input("ID del criticidad a editar: ")
            while True:
                print("¿Que desea cambiar?")
                print("1. Nombre")
                print("2. Descripcion")
                print("0. No cambiar nada")
                try :
                    opcion = int(input("Seleccione una opción: "))
                    while opcion < 0 or opcion > 2:
                        opcion=int(input("Error, ingrese una opcion valida ="))
                except ValueError:
                    opcion=int(input("Error, ingrese una opcion ="))
                if opcion == 0:
                    break
                elif opcion == 1:
                    nuevoElemento = input("Nuevo nombre: ")
                    param = "nombre"
                elif opcion == 2:
                    nuevoElemento = input("Nueva descripcion: ")
                    param = "descripcion"
                else:
                    print("Opción no válida")
                    input("Presione Enter para continuar...")
                db.editarCriticidad(idCriticidad,param,nuevoElemento)
                break
        elif opcion == 4:
            idCriticidad = input("Id del criticidad a eliminar: ")
            db.eliminarCriticidadPorId(idCriticidad)
        else:
            print("Opción no válida")
            input("Presione Enter para continuar...")


def ver_menu_filtro():
    while True:
        print("\nSeleccione un filtro para ver los tickets:")
        print("1. Fecha")
        print("2. Criticidad")
        print("3. Tipo de Ticket")
        print("4. Ejecutivo que abrió el ticket")
        print("5. Ejecutivo que cerró el ticket")
        print("6. Área")
        print("0. Cerrar")

        try:
            opcion = int(input("Seleccione una opción: "))
            while opcion < 0 or opcion > 6:
                opcion = int(input("Error, ingrese una opción válida: "))
        except ValueError:
            opcion = int(input("Error, ingrese una opción válida: "))

        if opcion == 0:
            break
        elif opcion == 1:  # FECHA
            while True:
                fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
                if len(fecha) == 10 and fecha[4] == '-' and fecha[7] == '-':
                    break
                else:
                    print("Formato de fecha incorrecto. Intente de nuevo.")
            db.ver_ticket(filtro='DATE(t.fechaCreacion)', valor=fecha)

        elif opcion == 2:  # CRITICIDAD
            opciones = db.busquedaFiltro('Criticidad', 'nombre')

            print("Seleccione una criticidad:")
            for i, nombre_criticidad in enumerate(opciones, 1):
                print(f"{i}. {nombre_criticidad}")
            opcion_seleccionada = int(input("Opción: ")) - 1
            seleccionado_nombre = opciones[opcion_seleccionada]
            db.ver_ticket(filtro='c.nombre', valor=seleccionado_nombre)

        elif opcion == 3:  # TIPOTICKET
            opciones = db.busquedaFiltro('TipoTicket', 'nombre')

            print("Seleccione un tipo de ticket:")
            for i, nombre_tipo in enumerate(opciones, 1):
                print(f"{i}. {nombre_tipo}")

            opcion_seleccionada = int(input("Opción: ")) - 1
            seleccionado_nombre = opciones[opcion_seleccionada]
            db.ver_ticket(filtro='tt.nombre', valor=seleccionado_nombre)

        elif opcion == 4:  # Ejecutivo que abrió el ticket
            opciones = db.busquedaFiltro('Ejecutivo', 'nombre')

            print("Lista de Ejecutivos:")
            for i, nombre_ejecutivo in enumerate(opciones, 1):
                print(f"{i}. {nombre_ejecutivo}")

            opcion_seleccionada = int(input("Opción: ")) - 1
            nombre_ejecutivo = opciones[opcion_seleccionada]
            db.ver_ticket(filtro='e.nombre', valor=nombre_ejecutivo)

        elif opcion == 5:  # Ejecutivo que cerró el ticket
            opciones = db.busquedaFiltro('Ejecutivo', 'nombre')

            print("Lista de Ejecutivos:")
            for i, nombre_ejecutivo in enumerate(opciones, 1):
                print(f"{i}. {nombre_ejecutivo}")

            opcion_seleccionada = int(input("Opción: ")) - 1
            nombre_ejecutivo = opciones[opcion_seleccionada]
            db.ver_ticket(filtro='e.nombre', valor=nombre_ejecutivo)

        elif opcion == 6:  # AREA
            opciones = db.busquedaFiltro('Area', 'nombre')

            print('Lista de Areas:')
            for i, nombre_area in enumerate(opciones, 1):
                print(f"{i}. {nombre_area}")

            opcion_seleccionada = int(input("Opción: ")) - 1
            nombre_area = opciones[opcion_seleccionada]
            db.ver_ticket(filtro='a.nombre', valor=nombre_area)