"""
    Clase de Madre de los usuarios con sus respectivos atributos y métodos
"""
class Usuario():
    def __init__(self,rut,nombre,apellidoPaterno,apellidoMaterno,nombreUsuario,contrasena):
        self.rut=rut
        self.nombre=nombre
        self.apellidoPaterno=apellidoPaterno
        self.apellidoMaterno=apellidoMaterno
        self.nombreUsuario=nombreUsuario
        self.contrasena=contrasena