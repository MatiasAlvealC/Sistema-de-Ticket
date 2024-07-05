import mysql.connector
from baseDeDatos.Database import Database
db = Database()



"""
    Clase de Ticket con sus respectivos atributos y métodos
"""


class Ticket:
    def __init__(self, database):
        self.db = database
        self.cursor = self.db.cursor()
    

    #Metodo para Crear un ticket
    def crearTicket(self):
        idTicket = input('Ingrese el id del ticket: ')
        rutUsuarioCreador =input('Rut del Creador del ticket: ')
        rutUsuarioCierre = input('Rut del Usuario que cierra: ')

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
        fechaCreacion = input('Ingrese fecha de creacion: ')
        estado = input('Ingrese estado del ticket: ')
        observacion = input('Ingrese Observacion')
        sql1='select * from ticket where idTicket='+repr(idTicket)
        
        try:
            self.cursor.execute(sql1)
            result = self.cursor.fetchall()
            if result == None:
                sql2 = (
                    "insert into ticket values("
                    + repr(idTicket) + ","
                    + repr(rutUsuarioCreador) + ","
                    + repr(rutUsuarioCierre) + ","
                    + repr(rutJefeMesa) + ","
                    + repr(idArea) + ","
                    + repr(idTipoTicket) + ","
                    + repr(idCriticidad) + ","
                    + repr(nombreCliente) + ","
                    + repr(apellidoPaternoCliente) + ","
                    + repr(apellidoMaternoCliente) + ","
                    + repr(rutCliente) + ","
                    + repr(telefonoCliente) + ","
                    + repr(correoCliente) + ","
                    + repr(detalleServicio) + ","
                    + repr(detalleProblematica) + ","
                    + repr(fechaCreacion) + ","
                    + repr(estado) + ","
                    + repr(observacion) + ")"
                    )
                try:
                    self.cursor.execute(sql2)
                    self.db.commit()
                    print('Ticket creado')
                except Exception as err:
                    self.db.rollback;
                    print(err)
            else:
                print('Ya existe ese ticket')
        except Exception as err:
            self.db.rollback()
            print(err)




    


  
"""
    Métodos del requerimiento funcional 2 (HU02)
    es hacer el constructor
"""

# Constructor



