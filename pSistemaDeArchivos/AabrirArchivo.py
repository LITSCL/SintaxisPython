from _io import open
import pathlib

ruta_absoluta: str = str(pathlib.Path().absolute())

#1. Abriendo el archivo (Permite trabajar con él).
archivo: object = open(ruta_absoluta + "/01-archivo.txt", "a+")

archivo.close()
