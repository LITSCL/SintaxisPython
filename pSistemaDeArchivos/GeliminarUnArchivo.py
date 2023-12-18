import pathlib
import os

ruta_archivo: str = str(pathlib.Path().absolute()) + "/04-G.txt"

#Eliminar el archivo.
os.remove(ruta_archivo)