import pathlib
import os

ruta_archivo: str = str(pathlib.Path().absolute()) + "/01-archivo.txt"

#Verificar si existe el archivo.
if (os.path.isfile(ruta_archivo)):
    print("Si existe el archivo")
else:
    print("No existe el archivo")