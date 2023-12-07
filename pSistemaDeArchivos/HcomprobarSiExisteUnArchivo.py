import pathlib
import os

rutaArchivo: str = str(pathlib.Path().absolute()) + "/01-archivo.txt"

#Verificar si existe el archivo.
if (os.path.isfile(rutaArchivo)):
    print("Si existe el archivo")
else:
    print("No existe el archivo")