"""
Vas a desarrollar un programa en Python que cumpla con las siguientes 
características:

**   Requerimientos:
-Base de datos: Crear una base de datos llamada 'inventario.db' para almacenar 
los datos de los productos. La tabla 'productos' debe contener las siguientes columnas:
-'id': Identificador único del producto (clave primaria, autoincremental).
-'nombre': Nombre del producto (texto, no nulo).
-'descripcion': Breve descripción del producto (texto).
-'cantidad': Cantidad disponible del producto (entero, no nulo).
-'precio': Precio del producto (real, no nulo).
-'categoria': Categoría a la que pertenece el producto (texto).

**   Funcionalidades de la aplicación

La aplicación debe permitir:
-Registrar nuevos productos.
-Visualizar datos de los productos registrados.
-Actualizar datos de productos, mediante su ID.
-Eliminación de productos, mediante su ID.
-Búsqueda de productos, mediante su ID. De manera opcional, se puede implementar la búsqueda por los campos nombre o categoría.
-Reporte de productos que tengan una cantidad igual o inferior a un límite especificado por el usuario o usuaria.

**    Interfaz de usuario
-Implementar una interfaz de usuario básica, para interactuar con la base de datos a través de la terminal. La interfaz debe incluir un menú principal con las opciones necesarias para acceder a cada funcionalidad descrita anteriormente.

"""

import db, gestor

db.crear_tabla()

#Mostramos nuestro menú...

while True:
    print()  #Dejo este print vacio para generar un salto de línea cada que inicie el Bucle.
    print("SISTEMA, GESTION DE INVENTARIO...")
    print("1- Registrar productos.")
    print("2- Visualizar todos los productos.")
    print("3- Actualizar precio de un producto.")
    print("4- Eliminar productos.")
    print("5- Buscar productos")
    print("6- Reporte de productos con stock limitado")
    print("7- Salir")

    opcion = input("Que acción desea realizar?: ").strip()

    match opcion:
        case "1":
            while True:
                nombre = input("Ingrese el nombre del producto(Escriba 'salir' para finalizar): ").strip()
                if nombre.lower() == 'salir':
                    break
                if not nombre:
                    print("NO DEBE HABER CAMPOS VACIOS.\n")
                    continue
            
                while True:
                    descripcion = input("Describa brevemente el producto ingresado: ").strip()
                    if not descripcion:
                        print("NO DEBE HABER CAMPOS VACIOS.\n")
                    else:
                        break
                    
                while True:  
                    try:
                        cantidad = int(input("Cantidad de stock hay para este producto?: "))
                        precio = float(input("Indique el precio del producto: "))

                        if not cantidad or not precio:
                            print("¡ERROR! NO DEBE HABER CAMPOS VACIOS.\n")
                        else:
                            break
                    except ValueError:
                        print("Los valores deben estar expresados en número.\n")

                while True:
                    categoria = input("A que categoria pertenece el producto?: ").strip()
                    if not categoria:
                        print("¡ERROR! NO DEBE HABER CAMPOS VACIOS.\n")
                    else:
                        break

                gestor.agregar_producto(nombre, descripcion, cantidad, precio, categoria)


        case "2":
            gestor.mostrar_productos()

        case "3":
            try:
                id_actualizar = int(input("Ingrese el ID del producto para actualizar: "))
                nuevo_precio = float(input("Ingrese el nuevo precio para actualizar: "))
                gestor.actualizar_precio_producto(id_actualizar, nuevo_precio)
            except ValueError:
                print("Los valores deben estar expresados en números.")

        case "4":
            try:
                id_eliminar = int(input("Ingrese el ID del producto para eliminar: "))
                gestor.eliminar_producto(id_eliminar)
            except ValueError:
                print("Los valores deben estar expresados en números.")

        case "5":
            try:
                id_buscar = int(input("Ingrese el ID del producto para buscar: "))
                gestor.buscar_producto(id_buscar)
            except ValueError:
                print("Los valores deben estar expresados en números.")

        case "6":
            try:
                limite = int(input("Indique el limite superior para el reporte: "))
                gestor.reporte_cantidad_producto(limite)
            except ValueError:
                print("Los valores deben estar expresados en números.")

        case "7":
            print("Saliendo del sistema...")
            break

        case _:
            print("Opción inválida... Seleccione nuevamente.")



