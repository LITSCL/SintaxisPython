import mysql.connector #Este módulo permite trabajar con el DBMS MySQL.

#2. Conectarse a la base de datos (Los parámetros se deben entregar así omo variables iniciadas dentro, con los nombres en inglés).
conexion: object = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "dbpruebas",
    port = 3306
)

#2. Cerrar la conexión.
conexion.close()