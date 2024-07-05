import mysql.connector

"""
    Conexion a la base de dato
"""

class Database():
    def __init__(self):
        self.conexion=mysql.connector.connect(
            host='localhost',
            user='root',
            password='q1q1q1q1',
            database='sistemticketdb')
        self.cursor=self.conexion.cursor()

    def cerrarBD(self):
        self.cursor.close()
        self.conexion.close()

    # metodos 
    
    """
         Métodos del requerimiento funcional 1 (HU01)
         M1: Jefe de  Mesa crear ejecutivo
            insert into ejecutivo value ()
        M2: Crear area, tipo de ticket y criticidad
            insert into area value()
            inser into tipoDeTicket
            insert into criticidad
        M3: editar area,tipodeticket y criticidad
            update XXXX blablablabla
        M4: eliminar area,tipodeticket y criticdad, pero si tiene asociado a un ticket no se podra
            delete blablablabla
            (if SELECT * FROM ticket WHERE idArea=XXX, si es nulo se puede eliminar, sino da un mensaje)
        M5: eliminar ejecutivo (cambiar su estado a desactivado)
            update blablablabla
    """
  
    
    
    
    
    
    # metodo que selecciona todos los ticket de la BD
    def selectTodos(self):
        sql = 'SELECT * FROM ticket'
        try:
            self.cursor.execute(sql)
            repu = self.cursor.fetchall()
            print('{:<6}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<25}{:<25}{:<25}{:<10}{:<12}{:<35}{:<100}{:<100}{:<12}{:<12}{:<10}{:<100}'.format(
                'ID', 'Usuario Creador', 'Usuario Cierre', 'Jefe Mesa', 'ID Área', 'ID Tipo', 'ID Criticidad', 'Nombre Cliente', 'Apellido Paterno', 'Apellido Materno', 'RUT', 'Teléfono', 'Correo', 'Detalle Servicio', 'Detalle Problema', 'Fecha Creación', 'Fecha Cierre', 'Estado', 'Observación'))
            for rep in repu:
                print('{:<6}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<25}{:<25}{:<25}{:<10}{:<12}{:<35}{:<100}{:<100}{:<12}{:<12}{:<10}{:<100}'.format(
                    rep[0], rep[1], rep[2], rep[3], rep[4], rep[5], rep[6], rep[7], rep[8], rep[9], rep[10], rep[11], rep[12], rep[13], rep[14], rep[15].strftime('%d/%m/%Y') if rep[15] else '', rep[16].strftime('%d/%m/%Y') if rep[16] else '', rep[17], rep[18]))
        except Exception as err:
            print(err)

    # metodo que selecciona un ticket a partir de idTicket
    def selectTicketPorIdTicket(self, idTicket):
        sql = 'SELECT * FROM ticket WHERE idTicket = {}'.format(idTicket)
        try:
            self.cursor.execute(sql)
            rep = self.cursor.fetchone()
            if rep is not None:
                print('{:<6}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<25}{:<25}{:<25}{:<10}{:<12}{:<35}{:<100}{:<100}{:<12}{:<12}{:<10}{:<100}'.format(
                    'ID', 'Usuario Creador', 'Usuario Cierre', 'Jefe Mesa', 'ID Área', 'ID Tipo', 'ID Criticidad', 'Nombre Cliente', 'Apellido Paterno', 'Apellido Materno', 'RUT', 'Teléfono', 'Correo', 'Detalle Servicio', 'Detalle Problema', 'Fecha Creación', 'Fecha Cierre', 'Estado', 'Observación'))
                print('{:<6}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<25}{:<25}{:<25}{:<10}{:<12}{:<35}{:<100}{:<100}{:<12}{:<12}{:<10}{:<100}'.format(
                    rep[0], rep[1], rep[2], rep[3], rep[4], rep[5], rep[6], rep[7], rep[8], rep[9], rep[10], rep[11], rep[12], rep[13], rep[14], rep[15].strftime('%d/%m/%Y') if rep[15] else '', rep[16].strftime('%d/%m/%Y') if rep[16] else '', rep[17], rep[18]))
            else:
                print('ID no existe')
        except Exception as err:
            print(err)

    def describe_ticket(self):
        sql = 'DESCRIBE ticket'
        try:
            self.cursor.execute(sql)
            rep = self.cursor.fetchall()
            print('{:<15}{:<20}{:<10}{:<10}{:<10}{:<10}'.format(
                'Field', 'Type', 'Null', 'Key', 'Default', 'Extra'))
            for row in rep:
                field, type_, null, key, default, extra = row
                default = default if default is not None else 'NULL'
                print('{:<15}{:<20}{:<10}{:<10}{:<10}{:<10}'.format(
                    field, type_, null, key, default, extra))
        except Exception as err:
            print(err)
    
    