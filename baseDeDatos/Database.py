import mysql.connector

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
    def crearEjecutivo(
        self,
        rut,
        nombre,
        apellido_paterno,
        apellido_materno,
        nombre_usuario,
        contrasena,
    ):
        sql = "INSERT INTO ejecutivo (rutEjecutivo, nombre, apellidoPaterno, apellidoMaterno, nombreUsuario, contraseña, estado) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        try:
            # Suponiendo que por defecto el estado es 'Activo'
            estado = "Activo"
            self.cursor.execute(
                sql,
                (
                    rut,
                    nombre,
                    apellido_paterno,
                    apellido_materno,
                    nombre_usuario,
                    contrasena,
                    estado,
                ),
            )
            self.conexion.commit()
            print("Ejecutivo creado correctamente.")
        except Exception as err:
            self.conexion.rollback()
            print(f"Error al crear ejecutivo: {err}")

    """ M2: Crear area, tipo de ticket y criticidad
            insert into area value()
            inser into tipoDeTicket
            insert into criticidad """

    # Método para crear una área
    def crearArea(self, nombre_area, descripcion):
        sql = "INSERT INTO area (nombreArea, descripcion) VALUES (%s, %s)"
        try:
            self.cursor.execute(sql, (nombre_area, descripcion))
            self.conexion.commit()
            print("Área creada correctamente.")
        except Exception as err:
            self.conexion.rollback()
            print(f"Error al crear área: {err}")

    # Método para crear tipo de ticket
    def crearTipoTicket(self, nombre_tipo, descripcion):
        sql = "INSERT INTO tipoDeTicket (nombreTipo, descripcion) VALUES (%s, %s)"
        try:
            self.cursor.execute(sql, (nombre_tipo, descripcion))
            self.conexion.commit()
            print("Tipo de ticket creado correctamente.")
        except Exception as err:
            self.conexion.rollback()
            print(f"Error al crear tipo de ticket: {err}")

    # Método para crear
    def crearCriticidad(self, nombre_criticidad, descripcion):
        sql = "INSERT INTO criticidad (nombre, descripcion) VALUES (%s, %s)"
        try:
            self.cursor.execute(sql, (nombre_criticidad, descripcion))
            self.conexion.commit()
            print("Criticidad creada correctamente.")
        except Exception as err:
            self.conexion.rollback()
            print(f"Error al crear criticidad: {err}")

    """M3: editar area,tipodeticket y criticidad
            update XXXX blablablabla """

    # Método de editar area
    def editarArea(self, id_area, nombre_area, descripcion):
        sql = "UPDATE area SET nombreArea = %s, descripcion = %s WHERE idArea = %s"
        try:
            self.cursor.execute(sql, (nombre_area, descripcion, id_area))
            self.conexion.commit()
            print("Área actualizada correctamente.")
        except Exception as err:
            self.conexion.rollback()
            print(f"Error al actualizar área: {err}")

    # Método de editar tipo de ticket
    def editarTipoTicket(self, id_tipo, nombre_tipo, descripcion):
        sql = "UPDATE tipoDeTicket SET nombreTipo = %s, descripcion = %s WHERE idTipoTicket = %s"
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
                        self.cursor.fetchall() != None
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



def iniciarSesion():
        # Conexión a la base de datos
        db = Database()
        try:
            # Pedir credenciales al usuario
            nombre_usuario = input("Ingrese su nombre de usuario: ")
            contrasena = input("Ingrese su contraseña: ")

            # Consultar en la tabla jefemesa
            cursor = db.cursor
            sql_jefe_mesa = (
                "SELECT * FROM jefemesa WHERE nombre = %s AND contrasena = %s"
            )
            cursor.execute(sql_jefe_mesa, (nombre_usuario, contrasena))
            jefe_mesa = cursor.fetchone()

            # Consultar en la tabla Ejecutivo
            sql_ejecutivo = "SELECT * FROM Ejecutivo WHERE nombreUsuario = %s AND contraseña = %s"
            cursor.execute(sql_ejecutivo, (nombre_usuario, contrasena))
            ejecutivo = cursor.fetchone()

            # Determinar el perfil del usuario
            if jefe_mesa:
                usuario = JefeDeMesa(*jefe_mesa)  # Instanciar objeto JefeDeMesa
                print("Inicio de sesión exitoso como Jefe de Mesa.")
                return usuario, "jefe_de_mesa"
            elif ejecutivo:
                usuario = Ejecutivo(*ejecutivo)  # Instanciar objeto Ejecutivo
                print("Inicio de sesión exitoso como Ejecutivo.")
                return usuario, "ejecutivo"
            else:
                print("Credenciales incorrectas. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, intente de nuevo.")
        except mysql.connector.Error as err:
            print(f"Error de MySQL: {err}")
            return None, None

finally:
    if cursor:
        cursor.close()
    if db:
        db.conexion.close()




