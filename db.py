import sqlite3

DB_NAME = "inventario.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def crear_tabla():
    #Conexión a la base de datos.
    conexion = conectar()
    cursor = conexion.cursor()

    #Creación de la tabla si no existe.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()