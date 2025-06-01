# PrimerawebNieto

Un sistema de gestión de escritores y libros desarrollado con Django.

Descripción

Primeraweb es una aplicación web diseñada para gestionar escritores y libros. Permite realizar el alta, listado y búsqueda de libros, todo dentro de una interfaz intuitiva con Bootstrap.

Características
 * Desplegables de escritores y libros con opciones de creación y listado.
 * Búsqueda de libros por nombre utilizando Django ORM.
 * Uso de plantillas HTML con Bootstrap para un diseño responsive.
 * Implementación de formularios para la gestión de registros.

Tecnologías utilizadas
- Python 3.13
- Django
- Bootstrap 5
- SQLite (o PostgreSQL, según configuración)
- HTML y CSS

Para crear un escritor o un libro, el usuario debe acceder a los formularios de alta, donde se ingresan los datos y se guardan en la base de datos.

Para que se pueda crear un libro, es necesario crear un escritor al cual asociar el libro

Flujo de Creación

1 Django carga un formulario (crear_escritor.html, crear_libro.html, crear_Estudiante.html).

2 El usuario ingresa la información requerida.

3 Al hacer clic en "Guardar", los datos se envían al servidor y se almacenan en la base de datos.

4 Después de guardar, el usuario es redirigido al listado


Flujo de Listado

1 Seleccionar la opcion Listar 

2 Al hacer clic el usuario es redirigido al listado Solictado

Flujo de Buscar

Desde la barra de navegacion se puede acceder al listado de los libros buscando en el cuadro de busqueda y prescionando en buscar
