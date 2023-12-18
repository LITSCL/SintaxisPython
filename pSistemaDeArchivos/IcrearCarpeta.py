import pathlib
import os

ruta_carpeta: str = str(pathlib.Path().absolute()) + "/IcrearCarpeta" + "/mi_carpeta"

if (os.path.isdir(ruta_carpeta) == False):
    os.mkdir(ruta_carpeta) #La función "mkdir", permite crear una carpeta, recibe como parámetro la ruta de la carpeta.
else:
    print("La carpeta ya existe")