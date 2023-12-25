import mysql.connector #Este módulo permite trabajar con el DBMS MySQL.

#1. Conectarse a la base de datos (Los parámetros se deben entregar así omo variables iniciadas dentro, con los nombres en inglés).
conexion: object = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "dbpruebas",
    port = 3306
)

#2. Crear el cursor.
cursor: object = conexion.cursor()

#3. Borrar un registro de la tabla "producto".
cursor.execute("DELETE FROM producto WHERE id = 6")

#4. Guardar cambios.
conexion.commit() #Siempre se debe hacer esto cuando se altere la base de datos.

#5. Cerrar la conexión.
conexion.close()