from _io import open
import pathlib

ruta_absoluta: str = str(pathlib.Path().absolute())

#1. Abriendo el archivo (Permite trabajar con él).
archivo: object = open(ruta_absoluta + "/01-archivo.txt", "a+")

#2. Escribiendo en el archivo.
archivo.write("Este es el primer texto" + "\n")

#3. Cerrando el archivo.
archivo.close()