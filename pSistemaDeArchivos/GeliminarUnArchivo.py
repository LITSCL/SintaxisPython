import pathlib
import os

rutaArchivo: str = str(pathlib.Path().absolute()) + "/04-G.txt"

#Eliminar el archivo.
os.remove(rutaArchivo)