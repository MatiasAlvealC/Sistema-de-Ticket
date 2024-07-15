import mysql.connector
from negocio.usuarios.JefeDeMesa import JefeDeMesa
from negocio.usuarios.Ejecutivo import Ejecutivo
from tabulate import tabulate
from datetime import datetime

"""
    Conexion a la base de dato
"""


class Database:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            #password="q1q1q1q1",
            password="nueva_contrasena",
            database="sistemticketdb",
        )
        self.cursor = self.conexion.cursor()

    def cerrarBD(self):
        self.cursor.close()
        self.conexion.close()

    # Funcion para iniciar sesion
    def iniciarSesion(self, nombre_usuario, contrasena):
        # Conexión a la base de datos
        try:
            sql_jefe = "SELECT * FROM jefemesa WHERE nombreUsuario = %s AND contrasena = %s"
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
        except ValueError:
            print("Entrada no válida. Por favor, intente de nuevo.")
            return None


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

    # Método para crear criticidad
    def crearCriticidad(self, idCriticidad, rutJefeMesa, nombre, descripcion):
        sql = "INSERT INTO criticidad VALUES(" + repr(idCriticidad) + "," + repr(rutJefeMesa) + "," + repr(nombre) + "," + repr(descripcion) + ")"
        try:
            self.cursor.execute(sql)
            self.conexion.commit()
            print("Criticidad creada correctamente.")
        except Exception as err:
            self.conexion.rollback()
            print(f"Error al crear criticidad: {err}")

    # Método para crear ticket
    def crearTicket(self,idTicket,rutUsuarioCreador,rutJefeMesa,idArea,idTipoTicket,idCriticidad,nombreCliente,apellidoPaternoCliente,apellidoMaternoCliente,rutCliente,telefonoCliente,correoCliente,detalleServicio,detalleProblematica,observacion):
        estado = "Abierto"
        fechaCreacion = datetime.now().strftime('%Y-%m-%d')  # Formato estándar de fecha y hora

        sql = (
            "INSERT INTO Ticket (idTicket, rutUsuarioCreador, rutJefeMesa, idArea, idTipoTicket, idCriticidad, nombreCliente, "
            "apellidoPaternoCliente, apellidoMaternoCliente, rutCliente, telefonoCliente, correoCliente, detalleServicio, "
            "detalleProblematica, fechaCreacion, estado, observacion) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )

        values = (
            idTicket, rutUsuarioCreador, rutJefeMesa, idArea, idTipoTicket, idCriticidad, nombreCliente,
            apellidoPaternoCliente, apellidoMaternoCliente, rutCliente, telefonoCliente, correoCliente,
            detalleServicio, detalleProblematica, fechaCreacion, estado, observacion
        )

        try:
            self.cursor.execute(sql, values)
            self.conexion.commit()
            print("ticket creado correctamente.")
        except Exception as err:
            self.conexion.rollback()
            print(f"Error al crear ticket: {err}")

    # Método de editar area
    def editarArea(self, id_area, param, cambio):
        sql1 = "select * from Area where idArea=" + repr(id_area)
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone() != None:  # valida que el area exista
                sql =  f"UPDATE area SET {param} = %s WHERE idArea = %s"
                try:
                    self.cursor.execute(sql,(cambio, id_area))
                    self.conexion.commit()
                    print("Área actualizada correctamente.")
                except Exception as err:
                    self.conexion.rollback()
                    print(f"Error al actualizar área: {err}")
            else:
                print("No existe dicha área")
        except Exception as err:
            print(err)

    # Método de editar tipo de ticket
    def editarTipoTicket(self, id_tipo, param, cambio):
        sql1 = "select * from tipoTicket where idTipoTicket=" + repr(id_tipo)
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone() != None:  # valida que el tipo de ticket exista
                sql =  f"UPDATE tipoTicket SET {param} = %s WHERE idTipoTicket = %s"
                try:
                    self.cursor.execute(sql,(cambio, id_tipo))
                    self.conexion.commit()
                    print("Tipo de ticket actualizada correctamente.")
                except Exception as err:
                    self.conexion.rollback()
                    print(f"Error al actualizar tipo de ticket: {err}")
            else:
                print("No existe dicha tipo de ticket")
        except Exception as err:
            print(err)

    # Método de editar criticidad
    def editarCriticidad(self,id_criticidad, param, cambio):
        sql1 = "select * from criticidad where idCriticidad=" + repr(id_criticidad)
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone() != None:  # valida que el tipo de ticket exista
                sql =  f"UPDATE criticidad SET {param} = %s WHERE idCriticidad = %s"
                try:
                    self.cursor.execute(sql,(cambio, id_criticidad))
                    self.conexion.commit()
                    print("Criticidad actualizada correctamente.")
                except Exception as err:
                    self.conexion.rollback()
                    print(f"Error al actualizar criticidad: {err}")
            else:
                print("No existe dicha criticidad")
        except Exception as err:
            print(err)

    # Método para actualizar el estado del ejecutivo de Desactivado
    # Que seria eliminarlo para la vista
    def EliminarEjecutivo(self,rutEjecutivo ):
        sql1 = "select * from Ejecutivo where rutEjecutivo=" + repr(rutEjecutivo)
        try:
            self.cursor.execute(sql1)
            rep = self.cursor.fetchone()
            if rep != None:
                nuevo_estado = "Desactivado"
                sql2 = (
                    "update Ejecutivo set estado="+repr(nuevo_estado)+" where rutEjecutivo="
                    + repr(rutEjecutivo)
                )
                try:
                    self.cursor.execute(sql2)
                    self.conexion.commit()
                    print("Ejecutivo eliminado")
                except Exception as err:
                    self.conexion.rollback()
                    print(err)
            else:
                print("No existe dicho ejecutivo")
        except Exception as err:
            print(err)
    # Método eliminación area

    def eliminarAreaPorId(self,idArea):
        sql1 = "select * from Area where idArea=" + repr(idArea)
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone() != None:  # valida que el area exista
                sql2 = "select * from ticket where idArea=" + repr(idArea)
                try:
                    self.cursor.execute(sql2)
                    if self.cursor.fetchall():  # si hay un área usandose en un ticket
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

    def eliminarTipoDeTicketPorId(self,idTipoTicket):
        sql1 = "select * from tipoTicket where idTipoTicket=" + repr(idTipoTicket)
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone() != None:  # valida que el area exista
                sql2 = "select * from ticket where idTipoTicket=" + repr(idTipoTicket)
                try:
                    self.cursor.execute(sql2)
                    if self.cursor.fetchall():  # si hay un tipo de ticket usandose en un ticket
                        print(
                            "No se puede eliminar, el tipo de ticket esta asociado ya un ticket"
                        )
                    else:
                        sql3 = "delete from tipoTicket where idTipoTicket=" + repr(idTipoTicket)
                        try:
                            self.cursor.execute(sql3)
                            self.conexion.commit()
                            print("Tipo de ticket eliminado correctamente.")
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

    def eliminarCriticidadPorId(self,idCriticidad):
        sql1 = "select * from criticidad where idCriticidad=" + repr(idCriticidad)
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone() != None:  # valida que el area exista
                sql2 = "select * from ticket where idCriticidad=" + repr(idCriticidad)
                try:
                    self.cursor.execute(sql2)
                    if self.cursor.fetchall():  # si hay un área usandose en un ticket
                        print(
                            "No se puede eliminar, la criticidad esta asociado ya un ticket"
                        )
                    else:
                        sql3 = "delete from criticidad where idCriticidad=" + repr(idCriticidad)
                        try:
                            self.cursor.execute(sql3)
                            self.conexion.commit()
                            print("Criticidad eliminada correctamente.")
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

    # funcion que muestra los ejecutivos 
    def mostrarEjectuvos(self):
        condicion = "Activo"
        sql = "SELECT e.rutEjecutivo,e.nombre,e.apellidoPaterno,e.apellidoMaterno,a.nombre as nombreArea FROM ejecutivo e, area a where a.idArea = e.idArea and e.estado ="+repr(condicion)
        try:
            self.cursor.execute(sql)
            respuesta = self.cursor.fetchall()
            print ("----- Ejecutivos -----")
            print(tabulate(respuesta, headers=['Rut', 'Nombre', 'Apellido Paterno','Apellido Materno','Area'], tablefmt='mixed_grid'))
            
        except Exception as err:
            print(err)

    # funcion que muestra las areas
    def mostrarAreas(self):
        sql = "SELECT idArea,nombre,descripcion FROM area"
        try:
            self.cursor.execute(sql)
            respuesta = self.cursor.fetchall()
            print ("----- Areas -----")
            print(tabulate(respuesta, headers=['ID', 'Nombre', 'Descripcion'], tablefmt='mixed_grid'))
            
        except Exception as err:
            print(err)

    # funcion que muestra los tipos de ticket
    def mostrarTipoTicketes(self):
        sql = "SELECT idTipoTicket,nombre,descripcion FROM tipoTicket"
        try:
            self.cursor.execute(sql)
            respuesta = self.cursor.fetchall()
            print ("----- Tipo de tickets -----")
            print(tabulate(respuesta, headers=['ID', 'Nombre', 'Descripcion'], tablefmt='mixed_grid'))
            
        except Exception as err:
            print(err)

    # funcion que muestra las criticidades
    def mostrarCriticidades(self):
        sql = "SELECT idCriticidad,nombre,descripcion FROM criticidad"
        try:
            self.cursor.execute(sql)
            respuesta = self.cursor.fetchall()
            print ("----- Criticidad -----")
            print(tabulate(respuesta, headers=['ID', 'Nombre', 'Descripcion'], tablefmt='mixed_grid'))
            
        except Exception as err:
            print(err)

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