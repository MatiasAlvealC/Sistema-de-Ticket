from baseDeDatos.Database import Database
from Interfaz.limpiarPantalla import *
from tabulate import tabulate
from datetime import datetime

db = Database()

def ejecutivoMenu(ejecutivo):
    while True:
        print("\n1. Ver tickets")
        print("2. Crear Ticket")
        print("0. Cerrar sesión")


        try:
            opcion = int(input("Seleccione una opción: "))
            while opcion < 0 or opcion > 4:
                opcion = int(input("Error, ingrese una opción válida: "))
        except ValueError:
            print("Error, ingrese un número válido.")


        limpiar_pantalla()  # Limpia la pantalla 
        # Manejo de opciones

        if opcion == 0:
            break
        elif opcion == 1:
            verTicketMenu(ejecutivo)
        elif opcion == 2:
            verCrearTicketMenu(ejecutivo)
        else:
            print("Opción no válida, por favor intente nuevamente.")

def verCrearTicketMenu(ejecutivo):
        # Datos para crear el ticket
        # Datos personales del cliente
        nombreCliente = input('Ingrese Nombre del Cliente: ')
        while nombreCliente == '':
            nombreCliente = input('Error, Ingrese Nombre del Cliente: ')

        apellidoPaternoCliente = input('Apellido Paterno: ')
        while apellidoPaternoCliente == '':
            apellidoPaternoCliente = input('Error, Apellido Paterno: ')

        apellidoMaternoCliente = input('Apellido Materno: ')
        while apellidoMaternoCliente == '':
            apellidoMaternoCliente = input('Error, Apellido Materno: ')

        rutCliente = input('Rut del Cliente: ')
        while rutCliente == '':
            rutCliente = input('Error, Rut del Cliente: ')

        telefonoCliente = input('Telefono del Cliente: ')
        while telefonoCliente== '':
            telefonoCliente = input('Error, Telefono del Cliente: ')

        correoCliente = input('Correo del Cliente: ')
        while correoCliente== '':
            correoCliente = input('Error, Correo del Cliente: ')

        # Datos sobre el ticket
        nombre_Area = input('Ingrese nombre area: ')
        while nombre_Area == '':
            nombre_Area = input('Error, Ingrese nombre area: ')

        nombre_TipoTicket = input('Ingrese nombre Tipo Ticket=')
        while nombre_TipoTicket == '':
            nombre_TipoTicket = input('Error, Ingrese nombre Tipo Ticket=')

        nombre_Criticidad = input('Ingrese nombre Criticidad: ')
        while nombre_Criticidad == '':
            nombre_Criticidad = input('Error, Ingrese nombre Criticidad: ')

        # Detalles de la atencion
        detalleServicio = input('Detalles del Servicio: ')
        while detalleServicio == '':
            detalleServicio = input('Error, Detalles del Servicio: ')

        detalleProblematica = input('Detalles de la problematica: ')
        while detalleProblematica == '':
            detalleProblematica = input('Error, Detalles de la problematica: ')

        resultado = db.crearTicket(ejecutivo.rut,nombre_Area,nombre_TipoTicket,nombre_Criticidad,nombreCliente,apellidoPaternoCliente,apellidoMaternoCliente,rutCliente,telefonoCliente,correoCliente,detalleServicio,detalleProblematica)

        limpiar_pantalla()  # Limpia la pantalla 
        
        #  PRE-VISUALIZACION del ticket
        # Previsualización en tabla
        datos = [
            ['Nombre Cliente', nombreCliente],
            ['Apellido Paterno Cliente', apellidoPaternoCliente],
            ['Apellido Materno Cliente', apellidoMaternoCliente],
            ['Rut Cliente', rutCliente],
            ['Teléfono Cliente', telefonoCliente],
            ['Correo Cliente', correoCliente],
            ['Area', nombre_Area],
            ['Tipo Ticket', nombre_TipoTicket],
            ['Criticidad', nombre_Criticidad],
            ['Detalles del Servicio', detalleServicio],
            ['Detalles de la Problemática', detalleProblematica]
        ]

        print("\nPrevisualización de datos ingresados:\n")
        print(tabulate(datos, headers=['Campo Agregado', 'Dato'], tablefmt='grid'))
        
        if resultado == 'creado':
            print(" Debe asignar a un área el ticket creado para ser resuelto")
            nuevoArea = input("A que área será asignado: ")
            while nuevoArea == '':
                nuevoArea = input("Error, A que área será asignado: ")

            try:
                idArea = db.buscarIdArea(nuevoArea)
                if idArea is not None:
                    idTicket = db.buscarIdTicket(rutCliente)
                    if idTicket is not None:
                        resultado = db.editarTicket(idTicket, "idArea", idArea)
                        if resultado == 'actualizado':
                            print("Se le ha asignado un área al ticket")
                            db.editarTicket(idTicket, "estado", 'A resolución')
                    else:
                        print("No se encontró ningún ticket para el cliente especificado.")
                else:
                    print("El área especificada no existe.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Ticket no creado, verifique que datos ingresado sean correctos")

def verTicketMenu(ejecutivo):
    while True:
        print("\n1. Ver tickets creados")
        print("2. Ver Tickets asignados")
        print("0. Volver al menu anterior")


        try:
            opcion = int(input("Seleccione una opción: "))
            while opcion < 0 or opcion > 2:
                opcion = int(input("Error, ingrese una opción válida: "))
        except ValueError:
            print("Error, ingrese un número válido.")

        limpiar_pantalla()  # Limpia la pantalla 

        if opcion == 0:
            break
        elif opcion == 1:
            limpiar_pantalla()  # Limpia la pantalla 
            db.mostrarTicketsPorCreador(ejecutivo.rut)
        elif opcion == 2:
            db.mostrarTicketsPorArea(ejecutivo.rut)
            try:
                respuesta = input("¿desea actualizar un ticket? (s/n): ").lower()
                while respuesta != 's' and respuesta != 'n':
                    print("respuesta inválida. por favor ingrese 's' para sí o 'n' para no.")
                    respuesta = input("¿desea actualizar un ticket? (s/n): ").lower()
            except ValueError:
                print("Error, ingrese s o n válido.")

            if respuesta == 's':
                idTicketEditar= input("Ingrese el id del ticket a Actualizar: ")
                while idTicketEditar == '':
                    idTicketEditar= input("Error, Ingrese el id del ticket a Actualizar: ")

                print("Cambiar estado")
                verEstadoMenu(idTicketEditar,ejecutivo.rut)
        else:
            print("Opción no válida, por favor intente nuevamente.")


def verEstadoMenu(idTicketEditar,rutEjecutivo):
    while True:
        print("\n1. No Aplicable")
        print("2.Resuelto")
        print("0. Volver al menu anterior")
        try:
            opcion = int(input("Seleccione una opción: "))
            while opcion < 0 or opcion > 2:
                opcion = int(input("Error, ingrese una opción válida: "))
        except ValueError:
            print("Error, ingrese un número válido.")
        
        limpiar_pantalla()  # Limpia la pantalla 
        
        if opcion == 0:
            break
        elif opcion == 1:
            nuevoEstado='No Aplicable'
        elif opcion == 2:
            nuevoEstado='Resuelto'
        else:
            print("Opción no válida, por favor intente nuevamente.")
        
        db.editarTicket(idTicketEditar,"estado",nuevoEstado)
        db.mostrarTicketsPorArea(rutEjecutivo)

        observacion =input("Debe agregar una observación: ")
        while observacion == '':
            observacion =input("Error, Debe agregar una observación: ")

        print("Se procede a cerrar el ticket ")
        nuevoEstado= 'Cerrado'
        fechaCierre = datetime.now().strftime('%Y-%m-%d')

        db.editarTicket(idTicketEditar,"estado",nuevoEstado)
        db.editarTicket(idTicketEditar,"rutUsuarioCierre",rutEjecutivo)
        db.editarTicket(idTicketEditar,"fechaCierre",fechaCierre)

        print("Ticket cerrado")
        break


