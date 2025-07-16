Sistema de Gestión de Inventario
Este proyecto es una aplicación desarrollada en Python que permite la gestión básica de un inventario de productos utilizando una base de datos SQLite.

📋 Descripción
La aplicación permite:

-Registrar nuevos productos con nombre, descripción, cantidad, precio y categoría.

-Visualizar todos los productos registrados.

-Actualizar el precio de un producto por su ID.

-Eliminar productos mediante su ID.

-Buscar productos por ID.

-Generar un reporte de productos con stock menor o igual a un límite definido.

Todos los datos se almacenan en la base de datos inventario.db, generada automáticamente al ejecutar el programa.

⚙️ Requisitos
-Python 3.x

-Módulos estándar: sqlite3 (incluido en la instalación de Python)

🚀 Ejecución
1- Clonar el repositorio o descargar los archivos.

2- Desde la terminal, ubicarse en la carpeta del proyecto.

3- Ejecutar el archivo principal:

python main.py

4- Seguir el menú interactivo en la terminal para gestionar el inventario.

📂 Estructura de archivos

inventario/
│
├── main.py        # Menú e interacción con el usuario
├── gestor.py      # Funciones para CRUD y reportes
├── db.py          # Creación de la base de datos y la tabla
└── README.md      # Documentación del proyecto

✏️ Nota
El proyecto funciona en terminal. Para futuras versiones podría incorporarse una interfaz gráfica con Tkinter o PyQt.

👨‍🏫 Autor
Juan Pericaguan
Estudiante de Python inicial
Correo: juanmiguel018@gmail.com