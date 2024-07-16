import mysql.connector
from negocio.usuarios.JefeDeMesa import JefeDeMesa
from negocio.usuarios.Ejecutivo import Ejecutivo
from tabulate import tabulate
from datetime import datetime
import hashlib
import pwinput  
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
    
    def login(self):
        nombre=input('Ingrese nombre del usuario=')
        password=pwinput.pwinput('Ingrese contraseña=')
        password = hashlib.md5(password.encode('utf-8')).hexdigest()
        return nombre,password


    # Funcion para iniciar sesion
    def iniciarSesion(self):#, nombre_usuario, contrasena):
        nombre_usuario,contrasena=self.login()
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
                estado = 'Activo'
                sql_ejecutivo = "SELECT * FROM Ejecutivo WHERE estado=%s AND nombreUsuario = %s AND contraseña = %s"
                self.cursor.execute(sql_ejecutivo, (estado,nombre_usuario, contrasena))
                ejecutivo = self.cursor.fetchone()
                if ejecutivo:  # valida que el ejecutivo exista
                    usuario = Ejecutivo(*ejecutivo)  # Instanciar objeto Ejecutivo
                    print("Inicio de sesión exitoso como Ejecutivo.")
                    input('Presione Enter para continuar...')
                    return usuario,'ejecutivo'              
                else:
                    print("Credenciales incorrectas. Intente nuevamente.")
                    return 'none','none'
        except:
            print("Entrada no válida. Por favor, intente de nuevo.")
            return None


    # Método para crear ejecutivo
    def crearEjecutivo(self, rutEjecutivo, rutJefeMesa, nombre_Area, estado, nombre, apellido_paterno, apellido_materno, nombre_usuario, contraseña):
        sql = "select idArea from area where nombre="+repr(nombre_Area)
        try:
            self.cursor.execute(sql)
            idArea_resultado = self.cursor.fetchone()
            if idArea_resultado != None:  # valida que nos entrege algo
                idArea = idArea_resultado[0]  # Extrae el valor del resultado
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
        except Exception as err:
            self.conexion.rollback()
            print(f"Error al crear encontrar area: {err}")

    # Método para crear una área
    def crearArea(self, rutJefeMesa, nombre, descripcion):
        sql = "INSERT INTO area VALUES(" + repr('null') +","+repr(rutJefeMesa) + "," + repr(nombre) + "," + repr(descripcion) + ")" 
        try:
            self.cursor.execute(sql)
            self.conexion.commit()
            print("Área creada correctamente.")
        except Exception as err:
            self.conexion.rollback()
            print(f"Error al crear área: {err}")

    # Método para crear tipo de ticket
    def crearTipoTicket(self, rutJefeMesa, nombre, descripcion):
        sql = "INSERT INTO tipoTicket VALUES(" + repr('null') + "," + repr(rutJefeMesa) + "," + repr(nombre) + "," + repr(descripcion) + ")"
        try:
            self.cursor.execute(sql)
            self.conexion.commit()
            print("Tipo de ticket creado correctamente.")
        except Exception as err:
            self.conexion.rollback()
            print(f"Error al crear tipo de ticket: {err}")

    # Método para crear criticidad
    def crearCriticidad(self, rutJefeMesa, nombre, descripcion):
        sql = "INSERT INTO criticidad VALUES(" + repr('null') + "," + repr(rutJefeMesa) + "," + repr(nombre) + "," + repr(descripcion) + ")"
        try:
            self.cursor.execute(sql)
            self.conexion.commit()
            print("Criticidad creada correctamente.")
        except Exception as err:
            self.conexion.rollback()
            print(f"Error al crear criticidad: {err}")

    # Método para crear ticket
    def crearTicket(self,rutUsuarioCreador,nombre_Area,nombre_TipoTicket,nombre_Criticidad,nombreCliente,apellidoPaternoCliente,apellidoMaternoCliente,rutCliente,telefonoCliente,correoCliente,detalleServicio,detalleProblematica):
        sql1 = "select idArea from area where nombre="+repr(nombre_Area)
        sql2 = "select idTipoTicket from tipoTicket where nombre="+repr(nombre_TipoTicket)
        sql3 = "select idCriticidad from criticidad where nombre="+repr(nombre_Criticidad)
        sql4 = "select rutJefeMesa from ejecutivo where rutEjecutivo="+repr(rutUsuarioCreador)

        try:
            self.cursor.execute(sql1)
            idArea_resultado = self.cursor.fetchone()
            
            self.cursor.execute(sql2)
            idTipoTicket_resultado = self.cursor.fetchone()
            
            self.cursor.execute(sql3)
            idCriticidad_resultado = self.cursor.fetchone()

            self.cursor.execute(sql4)
            rutJefeMesa_resultado = self.cursor.fetchone()

            if idArea_resultado is not None or idTipoTicket_resultado is not None or idCriticidad_resultado is not None or rutJefeMEsa_resultado is not None:  # valida que nos entrege algo
                idArea = idArea_resultado[0]  # Extrae el valor del resultado
                idTipoTicket = idTipoTicket_resultado[0]
                idCriticidad = idCriticidad_resultado[0]
                rutJefeMesa = rutJefeMesa_resultado[0]

                estado = "Abierto"
                fechaCreacion = datetime.now().strftime('%Y-%m-%d')  # Formato estándar de fecha y hora
                sql = (
                    "INSERT INTO Ticket (rutUsuarioCreador, rutJefeMesa, idArea, idTipoTicket, idCriticidad, nombreCliente, "
                    "apellidoPaternoCliente, apellidoMaternoCliente, rutCliente, telefonoCliente, correoCliente, detalleServicio, "
                    "detalleProblematica, fechaCreacion, estado) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                )

                values = (
                    rutUsuarioCreador, rutJefeMesa, idArea, idTipoTicket, idCriticidad, nombreCliente,
                    apellidoPaternoCliente, apellidoMaternoCliente, rutCliente, telefonoCliente, correoCliente,
                    detalleServicio, detalleProblematica, fechaCreacion, estado
                )

                try:
                    self.cursor.execute(sql, values)
                    self.conexion.commit()
                    print("ticket creado correctamente.")
                    return 'creado'
                except Exception as err:
                    self.conexion.rollback()
                    print(f"Error al crear ticket: {err}")
                    return 'no creado'
        except Exception as err:
            self.conexion.rollback()
            print(f"Error al crear encontrar area,tipo de ticket o criticidad: {err}")
            
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

    # función de editar ticket
    def editarTicket(self,id_ticket, param, cambio):
        sql1 = "select * from ticket where idTicket=" + repr(id_ticket)
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone() != None:  # valida que el ticket exista
                sql =  f"UPDATE ticket SET {param} = %s WHERE idticket= %s"
                try:
                    self.cursor.execute(sql,(cambio, id_ticket))
                    self.conexion.commit()
                    print("Ticket actualizado correctamente.")
                    return 'actualizado'
                except Exception as err:
                    self.conexion.rollback()
                    print(f"Error al actualizar ticket: {err}")
                    return 'no actualizado'
            else:
                print("No existe dicha ticket")
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
    
    # funcion que muestra los ticket por creador
    def mostrarTicketsPorCreador(self, rutEjecutivo):
        sql = "SELECT t.idTicket, a.nombre as nombreArea, tt.nombre as tipoTicket, c.nombre as criticidad, " \
            "t.detalleServicio, t.detalleProblematica, t.estado, t.observacion " \
            "FROM ticket t " \
            "JOIN area a ON t.idArea = a.idArea " \
            "JOIN tipoTicket tt ON t.idTipoTicket = tt.idTipoTicket " \
            "JOIN criticidad c ON t.idCriticidad = c.idCriticidad " \
            "WHERE t.rutUsuarioCreador = " + repr(rutEjecutivo) + " AND t.estado != 'Cerrado'"
        try:
            self.cursor.execute(sql)
            respuesta = self.cursor.fetchall()
            print("----- Tickets creados -----")
            print(tabulate(respuesta, headers=['ID', 'Area', 'Tipo de ticket', 'Criticidad', 'Detalle servicio', 'Detalle problematica', 'Estado', 'Observación'], tablefmt='mixed_grid'))
            
        except Exception as err:
            print(err)

    
    # funcion que muestra los ticket de un area especifica
    def mostrarTicketsPorArea(self, rutEjecutivo):
        sql1 = "SELECT idArea FROM ejecutivo WHERE rutEjecutivo=" + repr(rutEjecutivo)
        try:
            self.cursor.execute(sql1)
            idArea_resultado = self.cursor.fetchone()
            if idArea_resultado is not None:  # valida que nos entregue algo
                idArea = idArea_resultado[0]  # Extrae el valor del resultado

                sql2 = "SELECT t.idTicket, a.nombre as nombreArea, tt.nombre as tipoTicket, c.nombre as criticidad, " \
                    "t.detalleServicio, t.detalleProblematica, t.estado, t.observacion " \
                    "FROM ticket t " \
                    "JOIN area a ON t.idArea = a.idArea " \
                    "JOIN tipoTicket tt ON t.idTipoTicket = tt.idTipoTicket " \
                    "JOIN criticidad c ON t.idCriticidad = c.idCriticidad " \
                    "WHERE t.idArea=" + repr(idArea) + " AND t.estado != 'Cerrado'"

                try:
                    self.cursor.execute(sql2)
                    respuesta = self.cursor.fetchall()
                    print("----- Tickets creados -----")
                    print(tabulate(respuesta, headers=['ID', 'Area', 'Tipo de ticket', 'Criticidad', 'Detalle servicio', 'Detalle problematica', 'Estado', 'Observación'], tablefmt='mixed_grid'))

                except Exception as err:
                    print(err)
            else:
                print("No existe dicho ejecutivo con el rut especificado.")
        except Exception as err:
            print(err)

    ###########################
    #### HACE ALGO ESTE METODO???????????
    def ver_ticket(self, filtro,valor):
        

        base_sql = ("SELECT e.nombre AS EjecutivoCreador, t.fechaCreacion, tt.nombre AS tipoTicket, c.nombre AS criticidad, a.nombre AS area, t.estado "
               "FROM ticket t, ejecutivo e, tipoticket tt, criticidad c, area a "
               "WHERE t.rutUsuarioCreador = e.rutEjecutivo AND t.idTipoTicket = tt.idTipoTicket AND t.idCriticidad = c.idCriticidad AND t.idArea = a.idArea AND "
               f"{filtro} = %s")


        params = (valor,)

        try:
            self.cursor.execute(base_sql, params)
            tickets = self.cursor.fetchall()
            if tickets:
                headers = ['Ejecutivo Creador', 'Fecha Creación', 'Tipo Ticket', 'Criticidad', 'Área', 'Estado']
                print(tabulate(tickets, headers=headers, tablefmt='mixed_grid'))
            else:
                print("No se encontraron tickets para la opción seleccionada.")
        except Exception as err:
            self.conexion.rollback()
            print(f"Error al ejecutar la consulta: {err}")
        input('Presione enter para continuar')


    def buscarIdTicket(self,rutCliente):
        sql = "SELECT idTicket FROM ticket where rutCliente="+repr(rutCliente)
        try:
            self.cursor.execute(sql)
            respuesta = self.cursor.fetchone()
            return respuesta[0]
            
        except Exception as err:
            print(err)
            return 'none'
    def buscarIdArea(self,nombre):
        sql = "SELECT idArea FROM area where nombre="+repr(nombre)
        try:
            self.cursor.execute(sql)
            respuesta = self.cursor.fetchone()
            return respuesta[0]
            
        except Exception as err:
            print(err)
            return 'none'

    def busquedaFiltro(self, opcion, columna):

        sql = f"select {columna} from {opcion}"
        try:

            self.cursor.execute(sql)
            opciones = self.cursor.fetchall()
            resultados = tuple(opcion[0] for opcion in opciones)
            return resultados
        except Exception as err:
            
            self.conexion.rollback()
            print(f"error al encontrar: {err}")
            return ()



