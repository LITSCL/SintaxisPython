import mysql.connector #Este módulo permite trabajar con el DBMS MySQL.

#2. Conectarse a la base de datos (Los parámetros se deben entregar así omo variables iniciadas dentro, con los nombres en inglés).
conexion: object = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "dbpruebas",
    port = 3306
)

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