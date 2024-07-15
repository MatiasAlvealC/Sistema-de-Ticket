""" 
INSERT INTO Ticket  VALUES (
    1, -- idTicket
    '2-2', -- rutUsuarioCreador
    '2-2', -- rutUsuarioCierre
    '3-3', -- rutJefeMesa
    '1', -- idArea
    '1', -- idTipoTicket
    '1', -- idCriticidad
    'Juan', -- nombreCliente
    'Pérez', -- apellidoPaternoCliente
    'González', -- apellidoMaternoCliente
    '1-9', -- rutCliente
    '1234567890', -- telefonoCliente
    'juan.perez@example.com', -- correoCliente
    'Servicio de instalación', -- detalleServicio
    'Problema con la instalación', -- detalleProblematica
    '2024-07-15', -- fechaCreacion
    '2024-07-16', -- fechaCierre
    'Abierto', -- estado
    'Observaciones adicionales' -- observacion
);
"""



#INSERT INTO Ticket  VALUES (1,'2-2','2-2','3-3','1','1','1','Juan','Pérez','González','1-9','1234567890','juan.perez@example.com','Servicio de instalación','Problema con la instalación','2024-07-15','2024-07-16','Abierto','Observaciones adicionales');

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