

from baseDeDatos.Database import Database
db = Database()

def ejecutivoMenu():
    while True:
        print("\n1. Ver Tickets")
        print("2. Cambiar Estado del Ticket a 'Resuelto'")
        print("3. Cambiar Estado del Ticket a 'No aplicable'")
        print("4. Agregar Observación y Cerrar Ticket")
        print("0. Cerrar sesión")


        try:
            opcion = int(input("Seleccione una opción: "))
            while opcion < 0 or opcion > 4:
                opcion = int(input("Error, ingrese una opción válida: "))
            return opcion
        except ValueError:
            print("Error, ingrese un número válido.")



    # Manejo de opciones

        if opcion == 0:
            print('x')
        elif opcion == 1:
            print('x')
            # Ver tickets
        elif opcion == 2:
            # Cambiar estado del ticket a 'Resuelto'
            while True:
                try:
                    idTicket = input("Ingrese el ID del ticket: ")
                    if idTicket:  # Añade cualquier validación necesaria para ID
                        nuevo_estado = "Resuelto"
                        #db.cambiarEstadoTicket(idTicket, nuevo_estado)
                        break
                    else:
                        print("Error, ingrese un ID válido.")
                except ValueError:
                    print("Error, ingrese un ID válido.")
        elif opcion == 3:
            # Cambiar estado del ticket a 'No aplicable'
            while True:
                try:
                    idTicket = input("Ingrese el ID del ticket: ")
                    if idTicket:  # Añade cualquier validación necesaria para ID
                        nuevo_estado = "No aplicable"
                        #db.cambiarEstadoTicket(idTicket, nuevo_estado)
                        break
                    else:
                        print("Error, ingrese un ID válido.")
                except ValueError:
                    print("Error, ingrese un ID válido.")
        elif opcion == 4:
            # Agregar observación y cerrar ticket
            while True:
                try:
                    idTicket = input("Ingrese el ID del ticket: ")
                    if idTicket:  # Añade cualquier validación necesaria para ID
                        observacion = input("Ingrese la observación: ")
                        #db.agregarObservacionYCerrarTicket(idTicket, observacion)
                        break
                    else:
                        print("Error, ingrese un ID válido.")
                except ValueError:
                    print("Error, ingrese un ID válido.")
        else:
            print("Opción no válida, por favor intente nuevamente.")


   