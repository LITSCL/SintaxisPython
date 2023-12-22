import sqlite3 #Este módulo permite trabajar con el DBMS SQLite.
import pathlib

ruta_absoluta: str = str(pathlib.Path().absolute())

#1. Conectarse a la base de datos.
conexion: object = sqlite3.connect(ruta_absoluta + "/db/dbpruebas.db") #Para crear una conexión, se debe entregar la ruta del fichero, en caso de no existir, se crea automaticamente.

#2. Crear el cursor.
cursor: object = conexion.cursor()

#3. Obtener todos los registros de la tabla "producto".
cursor.execute("SELECT * FROM producto")
productos: list = cursor.fetchall() #La función "fetchall" convierte los registros obtenidos en objetos Python y los retorna en una lista con tuplas (Cada atributo del objeto va en un indice de la tupla).

for producto in productos:
    print(producto)
    
print("-----------------------------------")

for producto in productos:
    print("ID: " + str(producto[0]) + " NOMBRE: " + producto[1] + " DESCRIPCION: " + producto[2] + " PRECIO: " + str(producto[3]))

#4. Cerrar la conexión.
conexion.close()