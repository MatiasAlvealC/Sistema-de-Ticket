from baseDeDatos.Database import Database
from tabulate import tabulate
from datetime import datetime

db = Database()

def ejecutivoMenu():
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



        # Manejo de opciones

        if opcion == 0:
            break
        elif opcion == 1:
            verTicketMenu()
        elif opcion == 2:
            verCrearTicketMenu()
        else:
            print("Opción no válida, por favor intente nuevamente.")

def verCrearTicketMenu():
        idTicket = input('Ingrese el id del ticket: ')
        rutUsuarioCreador =input('Rut del Creador del ticket: ')

        rutJefeMesa = input('Ingrese Rut Jefe de Mesa: ')
        idArea = input('Ingrese id area: ')
        idTipoTicket = input('Ingrese id Tipo Ticket=')
        idCriticidad = input('Ingrese id Criticidad: ')

        nombreCliente = input('Ingrese Nombre del Cliente: ')
        apellidoPaternoCliente = input('Apellido Paterno: ')
        apellidoMaternoCliente = input('Apellido Materno: ')
        rutCliente = input('Rut del Cliente: ')
        telefonoCliente = input('Telefono del Cliente: ')
        correoCliente = input('Correo del Cliente: ')
        detalleServicio = input('Detalles del Servicio: ')
        detalleProblematica = input('Detalles de la problematica: ')
        resultado = db.crearTicket(idTicket,rutUsuarioCreador,rutJefeMesa,idArea,idTipoTicket,idCriticidad,nombreCliente,apellidoPaternoCliente,apellidoMaternoCliente,rutCliente,telefonoCliente,correoCliente,detalleServicio,detalleProblematica)

        #  PRE-VISUALIZACION del ticket
        # Previsualización en tabla
        datos = [
            ['ID Ticket', idTicket],
            ['Rut Ejecutivo Creador', rutUsuarioCreador],
            ['Rut Jefe de Mesa', rutJefeMesa],
            ['ID Area', idArea],
            ['ID Tipo Ticket', idTipoTicket],
            ['ID Criticidad', idCriticidad],
            ['Nombre Cliente', nombreCliente],
            ['Apellido Paterno Cliente', apellidoPaternoCliente],
            ['Apellido Materno Cliente', apellidoMaternoCliente],
            ['Rut Cliente', rutCliente],
            ['Teléfono Cliente', telefonoCliente],
            ['Correo Cliente', correoCliente],
            ['Detalles del Servicio', detalleServicio],
            ['Detalles de la Problemática', detalleProblematica]
        ]

        print("\nPrevisualización de datos ingresados:\n")
        print(tabulate(datos, headers=['Campo Agregado', 'Dato'], tablefmt='grid'))
        
        if resultado == 'creado':
            print(" Debe asignar a un área el ticket creado para ser resuelto")
            nuevoIdArea = input("A que área será asignado: ")
            resultado= db.editarTicket(idTicket,"idArea",nuevoIdArea)
            if resultado == 'actualizado':
                print("Se le ha asignado un área al ticket")
                db.editarTicket(idTicket,"estado",'A resolución')

def verTicketMenu():
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
        
        if opcion == 0:
            break
        elif opcion == 1:
            rutEjecutivo=input('Rut del ejecutivo: ')
            db.mostrarTicketsPorCreador(rutEjecutivo)
        elif opcion == 2:
            rutEjecutivo=input('Rut del ejecutivo: ')
            db.mostrarTicketsPorArea(rutEjecutivo)
            respuesta = input("¿Desea Actualizar un ticket? (s/n): ").lower()
            if respuesta == 's':
                idTicketEditar= input("Ingrese el id del ticket a Actualizar: ")
                print("Cambiar estado")
                verEstadoMenu(idTicketEditar,rutEjecutivo)
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
        print("Se procede a cerrar el ticket ")
        nuevoEstado= 'Cerrado'
        fechaCierre: datetime.now().strftime('%Y-%m-%d')

        db.editarTicket(idTicketEditar,"estado",nuevoEstado)
        db.editarTicket(idTicketEditar,"rutUsuarioCierre",rutEjecutivo)
        db.editarTicket(idTicketEditar,"fechaCierre",fechaCierre)

        print("Ticket cerrado")
        break
