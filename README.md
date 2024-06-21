# Sistema-de-Ticket
### Descripción del Sistema de Gestión de Tickets

El sistema de gestión de tickets para la consultora "Consúltenos" está diseñado para centralizar y agilizar la creación, asignación, seguimiento y resolución de tiques de atención. Este sistema reemplazará el proceso actual basado en planillas Excel, mejorando la eficiencia y accesibilidad para todos los usuarios. A continuación, se describen las funcionalidades y características clave del sistema:

#### Funcionalidades Principales

1. **Creación de Tiques:**
   - Los ejecutivos de la mesa de ayuda pueden crear tiques a través de un formulario en línea.
   - Los tiques incluyen los siguientes campos:
     - Nombre del cliente
     - RUT del cliente
     - Datos de contacto del cliente: Teléfono y correo electrónico
     - Tipo de tique (felicitación, consulta, reclamo, problema)
     - Criticidad (baja, media, alta)
     - Detalle del servicio
     - Detalle del problema
     - Área para derivar (si corresponde)

2. **Asignación y Gestión de Tiques:**
   - Los tiques quedan asignados al ejecutivo que los crea inicialmente.
   - El ejecutivo asigna el tique a un área específica para su resolución, cambiando su estado a "A resolución".
   - Ejecutivos de las áreas específicas pueden actualizar el estado del tique a "Resuelto" o "No aplicable" y agregar observaciones antes de cerrar el tique.

3. **Visualización y Seguimiento:**
   - Previsualización del tique creado para confirmación por parte del ejecutivo.
   - El jefe de mesa puede obtener listados de tiques filtrados por:
     - Fecha específica
     - Criticidad
     - Tipo de tique
     - Ejecutivo que abre el tique
     - Ejecutivo que cierra el tique
     - Área

4. **Gestión de Usuarios y Áreas:**
   - Sistema de autenticación con usuario y contraseña.
   - El jefe de mesa puede crear y editar usuarios del sistema, áreas, tipos de tique y criticidades.
   - No se permite eliminar áreas, tipos de tique o criticidades si existen tiques asociados.
   - La eliminación de un usuario solo desactiva su acceso, sin borrar los tiques creados por él.

5. **Roles de Usuario:**
   - Ejecutivos de mesa de ayuda: Pueden crear, asignar y gestionar tiques.
   - Ejecutivos de áreas específicas: Pueden actualizar el estado de los tiques y agregar observaciones.
   - Jefe de mesa: Tiene permisos adicionales para gestionar usuarios, áreas y ver reportes detallados de los tiques.

#### Interfaz de Usuario

1. **Panel de Creación de Tiques:**
   - Formulario intuitivo para la entrada de datos del cliente y detalles del tique.
   - Botón de previsualización para revisar el tique antes de su creación definitiva.

2. **Panel de Gestión de Tiques:**
   - Listado de tiques con opciones de filtrado y búsqueda avanzada.
   - Detalles visibles incluyen nombre del ejecutivo, fecha de creación, tipo de tique, criticidad, área de destino y estado.

3. **Panel de Administración:**
   - Opciones para crear y gestionar usuarios, áreas, tipos de tique y criticidades.
   - Visualización y edición de configuraciones del sistema.

#### Seguridad y Acceso

- Autenticación mediante usuario y contraseña.
- Diferenciación automática del tipo de usuario al iniciar sesión, mostrando las opciones correspondientes a su rol.
- Mecanismos de desactivación de usuarios sin afectar los datos históricos.

#### Mantenimiento y Evolución

- Sistema diseñado para permitir la adición de nuevas áreas, tipos de tique y criticidades sin necesidad de reestructuración significativa.
- Soporte para actualizaciones y mejoras continuas basadas en feedback de los usuarios.

### Beneficios Esperados

- Mejora en la eficiencia del proceso de creación y gestión de tiques.
- Acceso centralizado y en tiempo real a la información de los tiques.
- Reducción de errores y redundancias asociadas al manejo manual de planillas Excel.
- Facilita la toma de decisiones mediante reportes detallados y opciones de filtrado avanzadas.

Este sistema de gestión de tickets proporcionará una plataforma robusta y accesible para todos los usuarios de "Consúltenos", mejorando significativamente la calidad del servicio y la satisfacción del cliente.
