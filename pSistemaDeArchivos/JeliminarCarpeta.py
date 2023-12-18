import pathlib
import os

ruta_carpeta: str = str(pathlib.Path().absolute()) + "/mi_carpeta"

os.rmdir(ruta_carpeta) #La función "dmdir", permite eliminar una carpeta, recibe como parámetro la ruta de la carpeta.