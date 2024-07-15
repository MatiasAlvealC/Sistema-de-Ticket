import mysql.connector
from negocio.usuarios.JefeDeMesa import JefeDeMesa
from negocio.usuarios.Ejecutivo import Ejecutivo
from tabulate import tabulate

"""
    Conexion a la base de dato
"""
# este es un comentariooo
##
###
###
###
###


class Database:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="q1q1q1q1",
            database="sistemticketdb",
        )
        self.cursor = self.conexion.cursor()

    def cerrarBD(self):
        self.cursor.close()
        self.conexion.close()

    def iniciarSesion(self, nombre_usuario, contrasena):
        # Conexión a la base de datos
        try:
            sql_jefe = "SELECT * FROM jefemesa WHERE nombre = %s AND contrasena = %s"
            self.cursor.execute(sql_jefe, (nombre_usuario, contrasena))
            jefe_mesa = self.cursor.fetchone()
            if jefe_mesa:  # valida que el jefe exista
                usuario = JefeDeMesa(*jefe_mesa)  # Instanciar objeto JefeDeMesa
                print("Inicio de sesión exitoso como Jefe de Mesa.")
                input('Presione Enter para continuar...')
                return usuario,'jefe'
            else:
                # Consultar en la tabla Ejecutivo
                sql_ejecutivo = "SELECT * FROM Ejecutivo WHERE nombreUsuario = %s AND contraseña = %s"
                self.cursor.execute(sql_ejecutivo, (nombre_usuario, contrasena))
                ejecutivo = self.cursor.fetchone()
                if ejecutivo:  # valida que el ejecutivo exista
                    usuario = Ejecutivo(*ejecutivo)  # Instanciar objeto Ejecutivo
                    print("Inicio de sesión exitoso como Ejecutivo.")
                    input('Presione Enter para continuar...')
                    return usuario,'ejecutivo'              
                else:
                    print("Credenciales incorrectas. Intente nuevamente.")
                    return None
        except ValueError:
            print("Entrada no válida. Por favor, intente de nuevo.")
            return None

# Método para crear ejecutivo
    # Método para crear ejecutivo
# Método para crear ejecutivo
    def crearEjecutivo(self, rutEjecutivo, rutJefeMesa, idArea, estado, nombre, apellido_paterno, apellido_materno, nombre_usuario, contraseña):
        sql = "INSERT INTO ejecutivo (rutEjecutivo, rutJefeMesa, idArea, estado, nombre, apellidoPaterno, apellidoMaterno, nombreUsuario, contraseña) VALUES (" + repr(rutEjecutivo) + "," + repr(rutJefeMesa) + "," + repr(idArea) + "," + repr(estado) + "," + repr(nombre) + "," + repr(apellido_paterno) + "," + repr(apellido_materno) + "," + repr(nombre_usuario) + "," + repr(contraseña) + ")"
        try:
            # Suponiendo que por defecto el estado es 'Activo'
            estado = "Activo"
            self.cursor.execute(sql)
            self.conexion.commit()
            print("Ejecutivo creado correctamente.")
        except Exception as err:
            self.conexion.rollback()
            print(f"Error al crear ejecutivo: {err}")

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

    """
      Métodos del requerimiento funcional 1 (HU01)
         M1: Jefe de  Mesa crear ejecutivo
            insert into ejecutivo value ()"""

    # Método para crear ejecutivo

    """ M2: Crear area, tipo de ticket y criticidad
            insert into area value()
            inser into tipoDeTicket
            insert into criticidad """

    # Método para crear una área
    def crearArea(self,idArea, rutJefeMesa, nombre, descripcion):
        sql = "INSERT INTO area VALUES(" + repr(idArea) +","+repr(rutJefeMesa) + "," + repr(nombre) + "," + repr(descripcion) + ")" 
        try:
            self.cursor.execute(sql)
            self.conexion.commit()
            print("Área creada correctamente.")
        except Exception as err:
            self.conexion.rollback()
            print(f"Error al crear área: {err}")

    # Método para crear tipo de ticket
    def crearTipoTicket(self, idTipoTicket, rutJefeMesa, nombre, descripcion):
        sql = "INSERT INTO tipoTicket VALUES(" + repr(idTipoTicket) + "," + repr(rutJefeMesa) + "," + repr(nombre) + "," + repr(descripcion) + ")"
        try:
            self.cursor.execute(sql)
            self.conexion.commit()
            print("Tipo de ticket creado correctamente.")
        except Exception as err:
            self.conexion.rollback()
            print(f"Error al crear tipo de ticket: {err}")

    # Método para crear
    def crearCriticidad(self, idCriticidad, rutJefeMesa, nombre, descripcion):
        sql = "INSERT INTO criticidad VALUES(" + repr(idCriticidad) + "," + repr(rutJefeMesa) + "," + repr(nombre) + "," + repr(descripcion) + ")"
        try:
            self.cursor.execute(sql)
            self.conexion.commit()
            print("Criticidad creada correctamente.")
        except Exception as err:
            self.conexion.rollback()
            print(f"Error al crear criticidad: {err}")

    """M3: editar area,tipodeticket y criticidad
            update XXXX blablablabla """

    # Método de editar area
    def editarArea(self, id_area, nombre_area, descripcion):
        sql = "UPDATE area SET nombre = %s, descripcion = %s WHERE idArea = %s"
        try:
            self.cursor.execute(sql, (nombre_area, descripcion, id_area))
            self.conexion.commit()
            print("Área actualizada correctamente.")
        except Exception as err:
            self.conexion.rollback()
            print(f"Error al actualizar área: {err}")

    # Método de editar tipo de ticket
    def editarTipoTicket(self, id_tipo, nombre_tipo, descripcion):
        sql = "UPDATE tipoDeTicket SET nombre  = %s, descripcion = %s WHERE idTipoTicket = %s"
        try:
            self.cursor.execute(sql, (nombre_tipo, descripcion, id_tipo))
            self.conexion.commit()
            print("Tipo de ticket actualizado correctamente.")
        except Exception as err:
            self.conexion.rollback()
            print(f"Error al actualizar tipo de ticket: {err}")

    # Método de editar criticidad
        def editarCriticidad(self, id_criticidad, nombre_criticidad, descripcion):
            sql = "UPDATE criticidad SET nombre = %s, descripcion = %s WHERE idCriticidad = %s"
            try:
                self.cursor.execute(sql, (nombre_criticidad, descripcion, id_criticidad))
                self.conexion.commit()
                print("Criticidad actualizada correctamente.")
            except Exception as err:
                self.conexion.rollback()
                print(f"Error al actualizar criticidad: {err}")

    # Método eliminación area

    def eliminarAreaPorId(self):
        idArea = input("Id del área=")
        sql1 = "select * from Area where idArea=" + repr(idArea)
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone() != None:  # valida que el area exista
                sql2 = "select * from ticket where idArea=" + repr(idArea)
                try:
                    self.cursor.execute(sql2)
                    if (
                        self.cursor.fetchall() != None
                    ):  # si no hay un area usandose en un ticket
                        print(
                            "No se puede eliminar, el área esta asociado ya un ticket"
                        )
                    else:
                        sql3 = "delete from Area where idArea=" + repr(idArea)
                        try:
                            self.cursor.execute(sql3)
                            self.conexion.commit()
                            print("Área eliminada correctamente.")
                        except Exception as err:
                            self.conexion.rollback()
                            print(err)
                except Exception as err:
                    print(err)
            else:
                print("No existe dicha área")
        except Exception as err:
            print(err)

    # Método eliminación tipo de ticket

    def eliminarTipoDeTicketPorId(self):
        idTipoTicket = input("Id del tipo de ticket=")
        sql1 = "select * from TipoTicket where idTipoTicket=" + repr(idTipoTicket)
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone() != None:  # valida que el tipo de ticket exista
                sql2 = "select * from ticket where idTipoTicket=" + repr(idTipoTicket)
                try:
                    self.cursor.execute(sql2)
                    if (
                        self.cursor.fetchone() != None
                    ):  # si no hay un area usandose en un ticket
                        print(
                            "No se puede eliminar, el tipo de ticket esta asociado ya un ticket"
                        )
                    else:
                        sql3 = "delete from tipodeTicket where idTipoTicket=" + repr(
                            idTipoTicket
                        )
                        try:
                            self.cursor.execute(sql3)
                            self.conexion.commit()
                        except Exception as err:
                            self.conexion.rollback()
                            print(err)
                except Exception as err:
                    print(err)
            else:
                print("No existe dicho tipo de ticket")
        except Exception as err:
            print(err)

    # Método eliminación criticidad

    def eliminarCriticidadPorId(self):
        idCriticidad = input("Id de la criticidad=")
        sql1 = "select * from Criticidad where idCriticidad=" + repr(idCriticidad)
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone() != None:  # valida que la criticidad exista
                sql2 = "select * from Ticket where idCriticidad=" + repr(idCriticidad)
                try:
                    self.cursor.execute(sql2)
                    if (
                        self.cursor.fetchall() != None
                    ):  # si no hay un area usandose en un ticket
                        print(
                            "No se puede eliminar, la criticidad esta asociado ya un ticket"
                        )
                    else:
                        sql3 = "delete from Criticidad where idCriticidad=" + repr(
                            idCriticidad
                        )
                        try:
                            self.cursor.execute(sql3)
                            self.conexion.commit()
                        except Exception as err:
                            self.conexion.rollback()
                            print(err)
                except Exception as err:
                    print(err)
            else:
                print("No existe dicha criticidad")
        except Exception as err:
            print(err)

    ###########################################################################################################################################
    # Método para actualizar el estado del ejecutivo de Desactivado
    # Que seria eliminarlo para la vista
    def EliminarEjecutivo(self):
        rutEjecutivo = int(input("Ingrese el rut del ejecutivo que desea eliminar: "))
        sql1 = "select * from Ejecutivo where rutEjecutivo" + repr(rutEjecutivo)
        try:
            self.cursor.execute(sql1)
            rep = self.cursor.fetchone()
            if rep != None:
                sql2 = (
                    "update Ejecutivo set estado=Desactivado where rutEjecutivo="
                    + repr(rutEjecutivo)
                )
                try:
                    self.cursor.execute(sql2)
                    self.conexion.commit()
                except Exception as err:
                    self.conexion.rollback()
                    print(err)
            else:
                print("No existe dicho ejecutivo")
        except Exception as err:
            print(err)

    ###########################################################################################################################################

    # metodo que selecciona todos los ticket de la BD
    def selectTodos(self):
        sql = "SELECT * FROM ticket"
        try:
            self.cursor.execute(sql)
            repu = self.cursor.fetchall()
            print(
                "{:<6}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<25}{:<25}{:<25}{:<10}{:<12}{:<35}{:<100}{:<100}{:<12}{:<12}{:<10}{:<100}".format(
                    "ID",
                    "Usuario Creador",
                    "Usuario Cierre",
                    "Jefe Mesa",
                    "ID Área",
                    "ID Tipo",
                    "ID Criticidad",
                    "Nombre Cliente",
                    "Apellido Paterno",
                    "Apellido Materno",
                    "RUT",
                    "Teléfono",
                    "Correo",
                    "Detalle Servicio",
                    "Detalle Problema",
                    "Fecha Creación",
                    "Fecha Cierre",
                    "Estado",
                    "Observación",
                )
            )
            for rep in repu:
                print(
                    "{:<6}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<25}{:<25}{:<25}{:<10}{:<12}{:<35}{:<100}{:<100}{:<12}{:<12}{:<10}{:<100}".format(
                        rep[0],
                        rep[1],
                        rep[2],
                        rep[3],
                        rep[4],
                        rep[5],
                        rep[6],
                        rep[7],
                        rep[8],
                        rep[9],
                        rep[10],
                        rep[11],
                        rep[12],
                        rep[13],
                        rep[14],
                        rep[15].strftime("%d/%m/%Y") if rep[15] else "",
                        rep[16].strftime("%d/%m/%Y") if rep[16] else "",
                        rep[17],
                        rep[18],
                    )
                )
        except Exception as err:
            print(err)

    # metodo que selecciona un ticket a partir de idTicket
    def selectTicketPorIdTicket(self, idTicket):
        sql = "SELECT * FROM ticket WHERE idTicket = {}".format(idTicket)
        try:
            self.cursor.execute(sql)
            rep = self.cursor.fetchone()
            if rep is not None:
                print(
                    "{:<6}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<25}{:<25}{:<25}{:<10}{:<12}{:<35}{:<100}{:<100}{:<12}{:<12}{:<10}{:<100}".format(
                        "ID",
                        "Usuario Creador",
                        "Usuario Cierre",
                        "Jefe Mesa",
                        "ID Área",
                        "ID Tipo",
                        "ID Criticidad",
                        "Nombre Cliente",
                        "Apellido Paterno",
                        "Apellido Materno",
                        "RUT",
                        "Teléfono",
                        "Correo",
                        "Detalle Servicio",
                        "Detalle Problema",
                        "Fecha Creación",
                        "Fecha Cierre",
                        "Estado",
                        "Observación",
                    )
                )
                print(
                    "{:<6}{:<15}{:<15}{:<15}{:<10}{:<10}{:<10}{:<25}{:<25}{:<25}{:<10}{:<12}{:<35}{:<100}{:<100}{:<12}{:<12}{:<10}{:<100}".format(
                        rep[0],
                        rep[1],
                        rep[2],
                        rep[3],
                        rep[4],
                        rep[5],
                        rep[6],
                        rep[7],
                        rep[8],
                        rep[9],
                        rep[10],
                        rep[11],
                        rep[12],
                        rep[13],
                        rep[14],
                        rep[15].strftime("%d/%m/%Y") if rep[15] else "",
                        rep[16].strftime("%d/%m/%Y") if rep[16] else "",
                        rep[17],
                        rep[18],
                    )
                )
            else:
                print("ID no existe")
        except Exception as err:
            print(err)

    def describe_ticket(self):
        sql = "DESCRIBE ticket"
        try:
            self.cursor.execute(sql)
            rep = self.cursor.fetchall()
            print(
                "{:<15}{:<20}{:<10}{:<10}{:<10}{:<10}".format(
                    "Field", "Type", "Null", "Key", "Default", "Extra"
                )
            )
            for row in rep:
                field, type_, null, key, default, extra = row
                default = default if default is not None else "NULL"
                print(
                    "{:<15}{:<20}{:<10}{:<10}{:<10}{:<10}".format(
                        field, type_, null, key, default, extra
                    )
                )
        except Exception as err:
            print(err)

    def ver_ticket(self):
        while True: 
            filtro = input("Seleccione el filtro: \n1. Fecha específica\n2. Criticidad\n3. Tipo de ticket\n4. Ejecutivo que abre el ticket\n5. Ejecutivo que cierra el ticket\n6. Área\n0. Volver al menú\nOpción: ")
            #menu para interfaz
            if filtro == '0':
                break

            sql = ""
            params = ()

            if filtro == '1':
                while True:
                    fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
                    if len(fecha) == 10 and fecha[4] == '-' and fecha[7] == '-':
                        break
                    else:
                        print("Formato de fecha incorrecto. Intente de nuevo.")
                sql = ("SELECT DISTINCT Ticket.idTicket, Ejecutivo.nombre AS ejecutivoCreador, Ticket.fechaCreacion, TipoTicket.nombre AS tipoTicket, Criticidad.nombre AS criticidad, Area.nombre AS area, Ticket.estado "
                    "FROM Ticket, Ejecutivo, TipoTicket, Criticidad, Area "
                    "WHERE Ticket.rutUsuarioCreador = Ejecutivo.rutEjecutivo "
                    "AND Ticket.idTipoTicket = TipoTicket.idTipoTicket "
                    "AND Ticket.idCriticidad = Criticidad.idCriticidad "
                    "AND Ticket.idArea = Area.idArea "
                    "AND Ticket.fechaCreacion = %s")
                params = (fecha,)
            elif filtro == '2':
                self.cursor.execute("SELECT idCriticidad, nombre FROM Criticidad")
                opciones = self.cursor.fetchall()
                print("Seleccione una opción:")
                
                # Mostrar las opciones numeradas
                for i in range(len(opciones)):
                    id_criticidad = opciones[i][0]
                    nombre_criticidad = opciones[i][1]
                    print(f"{i + 1}. {nombre_criticidad}")
                
                # Solicitar al usuario que seleccione una opción
                opcion_seleccionada = int(input("Opción: ")) - 1
                seleccionado_id = opciones[opcion_seleccionada][0]
                
                sql = ("SELECT idTicket,rutUsuarioCreador,fechaCreacion,idTipoTicket,idCriticidad,idArea, estado FROM Ticket WHERE idCriticidad = %s")
                
                params = (seleccionado_id,)
                if sql:
                    try:
                        self.cursor.execute(sql, params)
                        tickets = self.cursor.fetchall()
                        print(tabulate(tickets, headers=['ID Ticket', 'Ejecutivo Creador', 'Area', 'Tipo Ticket', 'Criticidad', 'Nombre Cliente','Apellido Paterno','Apellido Materno','Detalle Servicio','Detalle Problematica','Fecha Creacion', 'Estado','Observacion'], tablefmt='mixed_grid'))
                        input("Presione Enter para continuar...")  # Pausar para permitir que el usuario vea los resultados
                    except Exception as err:
                        self.conexion.rollback()
                        print(err)





        



