import sqlite3 #Este módulo permite trabajar con el DBMS SQLite.
import pathlib

ruta_absoluta: str = str(pathlib.Path().absolute())

#1. Conectarse a la base de datos.
conexion: object = sqlite3.connect(ruta_absoluta + "/db/dbpruebas.db") #Para crear una conexión, se debe entregar la ruta del fichero, en caso de no existir, se crea automaticamente.

#2. Crear el cursor.
cursor: object = conexion.cursor()

#3. Borrar un registro de la tabla "producto".
cursor.execute("DELETE FROM producto WHERE id = 6")

#4. Guardar cambios.
conexion.commit() #Siempre se debe hacer esto cuando se altere la base de datos.

#5. Cerrar la conexión.
conexion.close()