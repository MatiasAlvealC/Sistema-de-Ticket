from negocio.usuarios.Usuario import Usuario

"""
    Clase de Jefe de Mesa con sus respectivos atributos y métodos
"""

class JefeDeMesa(Usuario):
    def __init__(self,rutJefeMesa,nombre,ApellidoPaterno,ApellidoMaternos,nombreUsuario,contrasena):
        super().__init__(rutJefeMesa,nombre,ApellidoPaterno,ApellidoMaternos,nombreUsuario,contrasena)
        
        
        
    # agregar los metodos
    # CRUD area,criticad, tipo de ticket, ticket y ejecutivos
        