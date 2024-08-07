from baseDeDatos.Database import *
from Interfaz.limpiarPantalla import *

db = Database()



# Funcion principal del menu ejecutivo
def jefeMenu(jefe): 
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
        
        limpiar_pantalla()  # Limpia la pantalla 

        # Manejo de opciones

        if opcion == 0:
            break
        elif opcion == 1:
            gestionarEjecutivo(jefe)
        elif opcion == 2:
            gestionarArea(jefe)
        elif opcion == 3:
            gestionarTipoTicket(jefe)
        elif opcion == 4:
            gestionarCriticidad(jefe)
        elif opcion == 5:
            menuFiltro()
        else:
            print("Opción no válida")
            input("Presione Enter para continuar...")


# Función gestionar ejecutivos

def gestionarEjecutivo(jefe):
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
    
        limpiar_pantalla()  # Limpia la pantalla 

        if opcion == 0:
            break
        elif opcion == 1:
            limpiar_pantalla()  # Limpia la pantalla 
            db.mostrarEjectuvos()
        elif opcion == 2:   

            rutEjecutivo = input("Rut del ejecutivo: ")
            while  rutEjecutivo == '':
                rutEjecutivo = input("Error, Rut del ejecutivo: ")

            nombre_Area = input('Nombre Area: ')
            while  nombre_Area == '':
                nombre_Area = input('Error, Nombre Area: ')

            nombre = input("Nombre del ejecutivo: ")
            while nombre == '':
                nombre = input("Error, Nombre del ejecutivo: ")

            apellido_paterno = input("Apellido paterno del ejecutivo: ")
            while  apellido_paterno == '':
                apellido_paterno = input("Error, Apellido paterno del ejecutivo: ")

            apellido_materno = input("Apellido materno del ejecutivo: ")
            while  apellido_materno== '':
                apellido_materno = input("Error, Apellido materno del ejecutivo: ")

            nombre_usuario = input("Nombre de usuario del ejecutivo: ")
            while nombre_usuario == '':
                nombre_usuario = input("Error, Nombre de usuario del ejecutivo: ")

            contrasena=pwinput.pwinput("Contraseña del ejecutivo: ")
            while  contrasena== '':
                contrasena=pwinput.pwinput("Error, Contraseña del ejecutivo: ")

            contrasena = hashlib.md5(contrasena.encode('utf-8')).hexdigest()
            estado = "Activo"  # Estado predeterminado

            res = db.crearEjecutivo(rutEjecutivo, jefe.rut, nombre_Area, estado, nombre, apellido_paterno, apellido_materno, nombre_usuario, contrasena)
            if res != 'exito':
                print("Error, se equivoco a ingresar el area")
            else:
                print("Ejecutivo creado con exito")
        
        elif opcion == 3:
            rutEjecutivo = input("Rut del ejecutivo a eliminar: ")
            while rutEjecutivo== '':
                rutEjecutivo = input("Error, Rut del ejecutivo a eliminar: ")

            db.EliminarEjecutivo(rutEjecutivo)
        else:
            print("Opción no válida")
            input("Presione Enter para continuar...")

# Función Gestionar Area

def gestionarArea(jefe):
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

        limpiar_pantalla()  # Limpia la pantalla 

        if opcion == 0:
            break
        elif opcion == 1:
            limpiar_pantalla()  # Limpia la pantalla 
            db.mostrarAreas()
        elif opcion == 2:
            print("----Nueva Área----")
            nombre_area = input("Nombre del área: ")
            while nombre_area== '':
                nombre_area = input("Error, Nombre del área: ")

            descripcion = input("Descripción del área: ")
            while descripcion== '':
                descripcion = input("Error, Descripción del área: ")

            db.crearArea(jefe.rut, nombre_area, descripcion)
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
                
                limpiar_pantalla()  # Limpia la pantalla 

                if opcion == 0:
                    break
                elif opcion == 1:
                    print("----Actualización Área----")
                    nuevoElemento = input("Nuevo nombre: ")
                    while nuevoElemento == '':
                        nuevoElemento = input("Error, Nuevo nombre: ")

                    param = "nombre"

                elif opcion == 2:
                    print("----Actualización Área----")
                    nuevoElemento = input("Nueva descripcion: ")
                    while nuevoElemento == '':
                        nuevoElemento = input("Error, Nueva descripcion: ")

                    param = "descripcion"
                else:
                    print("Opción no válida")
                    input("Presione Enter para continuar...")
                db.editarArea(idArea,param,nuevoElemento)
                break
        elif opcion == 4:
            idArea = input("Id del area a eliminar: ")
            while idArea == '':
                idArea = input("Error, Id del area a eliminar: ")

            db.eliminarAreaPorId(idArea)
        else:
            print("Opción no válida")
            input("Presione Enter para continuar...")


# Función Gestionar tipode ticket

def gestionarTipoTicket(jefe):
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

        limpiar_pantalla()  # Limpia la pantalla 

        if opcion == 0:
            break
        elif opcion == 1:
            limpiar_pantalla()  # Limpia la pantalla 
            db.mostrarTipoTicketes()
        elif opcion == 2:
            print("----Nuevo Tipo de Ticket----")
            nombre_tipoTicket = input("Nombre del tipo de ticket: ")
            while nombre_tipoTicket == '':
                nombre_tipoTicket = input("Error,Nombre del tipo de ticket: ")
            descripcion = input("Descripción del tipo de ticket: ")
            while descripcion == '':
                descripcion = input("Error, Descripción del tipo de ticket: ")
            db.crearTipoTicket(jefe.rut, nombre_tipoTicket, descripcion)
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

                limpiar_pantalla()  # Limpia la pantalla 

                if opcion == 0:
                    break
                elif opcion == 1:
                    print("----Actualización Tipo de Ticket----")
                    nuevoElemento = input("Nuevo nombre: ")
                    while nuevoElemento == '':
                        nuevoElemento = input("Error, Nuevo nombre: ")

                    param = "nombre"
                elif opcion == 2:
                    print("----Actualización Tipo de Ticket----")
                    nuevoElemento = input("Nueva descripcion: ")
                    while nuevoElemento == '':
                        nuevoElemento = input("Error, Nueva descripcion: ")

                    param = "descripcion"
                else:
                    print("Opción no válida")
                    input("Presione Enter para continuar...")
                db.editarTipoTicket(idTipoTicket,param,nuevoElemento)
                break
        elif opcion == 4:
            idArea = input("Id del tipo de ticket a eliminar: ")
            while idArea == '':
                idArea = input("Error, Id del tipo de ticket a eliminar: ")

            db.eliminarTipoDeTicketPorId(idTipoTicket)
        else:
            print("Opción no válida")
            input("Presione Enter para continuar...")

# Función Gestionar Criticidad

def gestionarCriticidad(jefe):
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

        limpiar_pantalla()  # Limpia la pantalla 

        if opcion == 0:
            break
        elif opcion == 1:
            limpiar_pantalla()  # Limpia la pantalla 
            db.mostrarCriticidades()
        elif opcion == 2:
            print("----Nueva Criticidada----")
            nombre_criticidad = input("Nombre de la criticidad: ")
            while nombre_criticidad == '':
                nombre_criticidad = input("Error, Nombre de la criticidad: ")

            descripcion = input("Descripción de la criticidad: ")
            while descripcion == '':
                descripcion = input("Descripción de la criticidad: ")

            db.crearCriticidad(jefe.rut, nombre_criticidad, descripcion)
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
                
                limpiar_pantalla()  # Limpia la pantalla 
                
                if opcion == 0:
                    break
                elif opcion == 1:
                    print("----Actualización Criticidad----")
                    nuevoElemento = input("Nuevo nombre: ")
                    while nuevoElemento == '':
                        nuevoElemento = input("Error, Nuevo nombre: ")

                    param = "nombre"
                elif opcion == 2:
                    print("----Actualización Criticidad----")
                    nuevoElemento = input("Nueva descripcion: ")
                    while nuevoElemento == '':
                        nuevoElemento = input("Error, Nueva descripcion: ")

                    param = "descripcion"
                else:
                    print("Opción no válida")
                    input("Presione Enter para continuar...")
                db.editarCriticidad(idCriticidad,param,nuevoElemento)
                break
        elif opcion == 4:
            idCriticidad = input("Id del criticidad a eliminar: ")
            while idCriticidad == '':
                idCriticidad = input("Error, Id del criticidad a eliminar: ")

            db.eliminarCriticidadPorId(idCriticidad)
        else:
            print("Opción no válida")
            input("Presione Enter para continuar...")

# Función para el menu de filtro de ticket
def menuFiltro():
    while True:
        limpiar_pantalla()  # Limpia la pantalla 
        print("Seleccione un filtro para ver los tickets:")
        print("\n1. Fecha")
        print("2. Criticidad")
        print("3. Tipo de Ticket")
        print("4. Ejecutivo que abrió el ticket")
        print("5. Ejecutivo que cerró el ticket")
        print("6. Área")
        print("0. Volver al menu anterior")

        try:
            opcion = int(input("Seleccione una opción: "))
            while opcion < 0 or opcion > 6:
                opcion = int(input("Error, ingrese una opción válida: "))
        except ValueError:
            opcion = int(input("Error, ingrese una opción válida: "))

        limpiar_pantalla()  # Limpia la pantalla 

        if opcion == 0:
            break
        elif opcion == 1:  # FECHA
            while True:
                fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
                while fecha == '':
                    fecha = input("Error, Ingrese la fecha (YYYY-MM-DD): ")
                if len(fecha) == 10 and fecha[4] == '-' and fecha[7] == '-':
                    break
                else:
                    print("Formato de fecha incorrecto. Intente de nuevo.")
            
            limpiar_pantalla()  # Limpia la pantalla 
            print("Mostrar tickets filtrados por fecha")
            db.ver_ticket(filtro='DATE(t.fechaCreacion)', valor=fecha)

        elif opcion == 2:  # CRITICIDAD
            opciones = db.busquedaFiltro('Criticidad', 'nombre')

            print("Seleccione una criticidad:")
            for i, nombre_criticidad in enumerate(opciones, 1):
                print(f"{i}. {nombre_criticidad}")
            opcion_seleccionada = (input("Opción: ")) 
            try: 
                while opcion_seleccionada == '':
                    opcion_seleccionada = (input("Error, Opción: "))
                opcion_seleccionada = int(opcion_seleccionada)- 1
                limpiar_pantalla()  # Limpia la pantalla 
                seleccionado_nombre = opciones[opcion_seleccionada]
                print(f"Mostrar tickets filtrados por criticidad: {seleccionado_nombre}")
                db.ver_ticket(filtro='c.nombre', valor=seleccionado_nombre)
            except ValueError:
                print("Opcion mal ingresada, ingrese un numero")
            

        elif opcion == 3:  # TIPOTICKET
            opciones = db.busquedaFiltro('TipoTicket', 'nombre')

            print("Seleccione un tipo de ticket:")
            for i, nombre_tipo in enumerate(opciones, 1):
                print(f"{i}. {nombre_tipo}")
            try:
                opcion_seleccionada = (input("Opción: ")) 
                while opcion_seleccionada == '':
                    opcion_seleccionada = (input("Error, Opción: "))
                opcion_seleccionada = int(opcion_seleccionada)- 1
                limpiar_pantalla()  # Limpia la pantalla 
                seleccionado_nombre = opciones[opcion_seleccionada]
                print(f"Mostrar tickets filtrados por tipo de ticket: {seleccionado_nombre}")
                db.ver_ticket(filtro='tt.nombre', valor=seleccionado_nombre)
            except ValueError:
                print("Opcion mal ingresada, ingrese un numero")
            

        elif opcion == 4:  # Ejecutivo que abrió el ticket
            opciones = db.busquedaFiltro('Ejecutivo', 'nombre')

            print("Lista de Ejecutivos:")
            for i, nombre_ejecutivo in enumerate(opciones, 1):
                print(f"{i}. {nombre_ejecutivo}")

            try:
                opcion_seleccionada = (input("Opción: ")) 
                while opcion_seleccionada == '':
                    opcion_seleccionada = (input("Error, Opción: "))
                opcion_seleccionada = int(opcion_seleccionada)- 1

                limpiar_pantalla()  # Limpia la pantalla 

                nombre_ejecutivo = opciones[opcion_seleccionada]
                print(f"Mostrar tickets filtrados por ejecutivo que abrió: {nombre_ejecutivo}")
                db.ver_ticket(filtro='e.nombre', valor=nombre_ejecutivo)
            except ValueError:
                print("Opcion mal ingresada, ingrese un numero")

        elif opcion == 5:  # Ejecutivo que cerró el ticket
            opciones = db.busquedaFiltro('Ejecutivo', 'nombre', "rutEjecutivo IN (SELECT rutUsuarioCierre FROM Ticket WHERE estado = 'Cerrado')") #Busqueda en base de datos
            
            print("Lista de Ejecutivos que cerraron tickets:")
            for i, nombre_ejecutivo in enumerate(opciones, 1):#Muestra la lista de nombres de ejecutivo que cerraron tickets
                print(f"{i}. {nombre_ejecutivo}")

            while True:
                try:
                    opcion_seleccionada = int(input("Opción: ")) - 1 #Este codigo verifica si la opcion seleccionada esta entre las opciones 
                    if 0 <= opcion_seleccionada < len(opciones):
                        break
                    else:
                        print("Opción no válida. Intente de nuevo.")
                except ValueError:
                    print("Error, ingrese un número válido")

            limpiar_pantalla()  # Limpia la pantalla 

            nombre_ejecutivo = opciones[opcion_seleccionada] #Obtiene el nombre del ejecutivo que cerro el ticket mostrado en la lista
            print(f"Mostrar tickets filtrados por ejecutivo que cerró: {nombre_ejecutivo}") 
            db.ver_ticketCerrado(filtro='e.nombre', valor=nombre_ejecutivo) #Se llama a la funcion ver_ticket para realizar una busqueda en la base de datos que muestre el nombre del ejecutivo que cerro el ticket.

        elif opcion == 6:  # AREA
            opciones = db.busquedaFiltro('Area', 'nombre')

            print('Lista de Areas:')
            for i, nombre_area in enumerate(opciones, 1):
                print(f"{i}. {nombre_area}")

            try:
                opcion_seleccionada = (input("Opción: ")) 
                while opcion_seleccionada == '':
                    opcion_seleccionada = (input("Error, Opción: "))
                opcion_seleccionada = int(opcion_seleccionada)- 1

                limpiar_pantalla()  # Limpia la pantalla 

                nombre_area = opciones[opcion_seleccionada]
                print(f"Mostrar tickets filtrados por área: {nombre_area}")
                db.ver_ticket(filtro='a.nombre', valor=nombre_area)
            except ValueError:
                print("Error, ingrese un número válido")
        else:
            print("Opción no válida")
            input("Presione Enter para continuar...")