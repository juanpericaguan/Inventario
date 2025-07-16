import db

#Empezamos a definir las funciones

#Función 1 para agregar productos...
def agregar_producto(nombre, descripcion, cantidad, precio, categoria):
    conexion = db.conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)''', (nombre, descripcion, cantidad, precio, categoria))
    conexion.commit()
    conexion.close()
    print("Producto agregado correctamente.\n")


#Funcion 2 Visualizar datos de los productos registrados.
def mostrar_productos():
    conexion = db.conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()

    print("\nMostrando los productos registrados:")
    for producto in productos:
        mostrar_detalles_producto(producto)

#Función 3 Actualizar precio de los productos, mediante su ID.
def actualizar_precio_producto(id_producto, nuevo_precio):
    conexion = db.conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        UPDATE productos SET precio = ? WHERE id = ?
''', (nuevo_precio, id_producto))
    conexion.commit()
    conexion.close()
    print("Precio actualizado correctamente.\n")


#Función 4 Eliminar productos mediante su ID.
def eliminar_producto(id_producto):
    conexion = db.conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        DELETE FROM productos WHERE id = ?
''', (id_producto,))
    conexion.commit()
    conexion.close()
    print("Producto eliminado correctamente.\n")

#Función 5. Buscar producto mediante su ID.
def buscar_producto(id_producto):
    conexion = db.conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        SELECT * FROM productos WHERE id = ?
''', (id_producto,))
    producto = cursor.fetchone()
    conexion.close()

    if producto:
        print("\nProducto encontrado:")
        mostrar_detalles_producto(producto)
    else:
        print("Producto no encontrado.")


#Función 6. Reporte de productos que tengan una cantidad igual o inferior a un límite dado por el usuario.
def reporte_cantidad_producto(limite):
    conexion = db.conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    productos = cursor.fetchall()
    conexion.close()

    if productos:
        print(f"\nProductos con cantidad menor o igual a {limite}:")
        for producto in productos:
            mostrar_detalles_producto(producto)

    else:
        print(f"\nNo hay productos con cantidad menor o igual a {limite}.")



#Funcion para evitar repetir impresiones...
def mostrar_detalles_producto(producto):
    print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, "
          f"Cantidad: {producto[3]}, Precio: {producto[4]}, Categoria: {producto[5]}")



