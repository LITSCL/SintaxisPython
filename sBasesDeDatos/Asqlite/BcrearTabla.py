import sqlite3 #Este módulo permite trabajar con el DBMS SQLite.
import pathlib

rutaAbsoluta: str = str(pathlib.Path().absolute())

#1. Conectarse a la base de datos.
conexion: object = sqlite3.connect(rutaAbsoluta + "/db/dbpruebas.db") #Para crear una conexión, se debe entregar la ruta del fichero, en caso de no existir, el fichero se crea automaticamente.

#2. Crear el cursor.
cursor: object = conexion.cursor()

#3. Crear una tabla.
cursor.execute("""
    CREATE TABLE producto(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nombre VARCHAR(255), 
    descripcion TEXT, 
    precio INT 
    );"""
)

#4. Guardar cambios.
conexion.commit() #Siempre se debe hacer esto cuando se altere la base de datos.

#5. Cerrar la conexión.
conexion.close()

