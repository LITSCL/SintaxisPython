import pathlib
import os

rutaCarpeta: str = str(pathlib.Path().absolute()) + "/IcrearCarpeta" + "/mi_carpeta"

if (os.path.isdir(rutaCarpeta) == False):
    os.mkdir(rutaCarpeta) #La función "mkdir", permite crear una carpeta, recibe como parámetro la ruta de la carpeta.
else:
    print("La carpeta ya existe")