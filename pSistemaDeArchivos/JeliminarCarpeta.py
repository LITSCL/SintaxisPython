import pathlib
import os

rutaCarpeta: str = str(pathlib.Path().absolute()) + "/mi_carpeta"

os.rmdir(rutaCarpeta) #La función "dmdir", permite eliminar una carpeta, recibe como parámetro la ruta de la carpeta.