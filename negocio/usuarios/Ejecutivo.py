from Usuario import *
"""
    Clase de Ejecutivo con sus respectivos atributos y métodos
"""

class Ejecutivo(Usuario):
    def __init__(self,rutEjecutivo,nombre,ApellidoPaterno,ApellidoMaternos,nombreUsuario,contrasena,estado,idArea,rutJefeMesa):
        super().__init__(rutEjecutivo,nombre,ApellidoPaterno,ApellidoMaternos,nombreUsuario,contrasena)
        self.estado=estado
        self.idArea=idArea
        self.rutJefeMesa=rutJefeMesa
        