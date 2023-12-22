import sqlite3 #Este módulo permite trabajar con el DBMS SQLite.
import pathlib

ruta_absoluta: str = str(pathlib.Path().absolute())

#1. Conectarse a la base de datos.
conexion: object = sqlite3.connect(ruta_absoluta + "/db/dbpruebas.db") #Para crear una conexión, se debe entregar la ruta del fichero, en caso de no existir, se crea automaticamente.

#2. Crear el cursor.
cursor: object = conexion.cursor()

#3. Insertar un registro en la tabla "producto".
cursor.execute("INSERT INTO producto VALUES(null, 'Producto 1', 'Mi Descripcion 1', 3500)")
cursor.execute("INSERT INTO producto VALUES(null, 'Producto 2', 'Mi Descripcion 2', 4500)")
cursor.execute("INSERT INTO producto VALUES(null, 'Producto 3', 'Mi Descripcion 3', 5500)")

productos: list = [
    ("Producto 4", "Mi Descripcion 4", 6500),
    ("Producto 5", "Mi Descripcion 5", 7500),
    ("Producto 6", "Mi Descripcion 6", 8500),
]

#4. Insertar una lista con registros (Cada registro debe estar organizado como tupla).
cursor.executemany("INSERT INTO producto VALUES (null, ?, ?, ?)", productos) #Cada indice de la tupla hace referencia a un signo ? (La referencia se hace en orden).

#5. Guardar cambios.
conexion.commit() #Siempre se debe hacer esto cuando se altere la base de datos.

#6. Cerrar la conexión.
conexion.close()