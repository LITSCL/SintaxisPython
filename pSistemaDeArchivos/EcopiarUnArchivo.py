import pathlib
import shutil

ruta_origen: str = str(pathlib.Path().absolute()) + "/02-E.txt"
ruta_destino: str = str(pathlib.Path().absolute()) + "/EcopiarUnArchivo/02-E_copia.txt"

#Copiar y pegar archivo.
shutil.copyfile(ruta_origen, ruta_destino) #La función "copyfile", permite copiar un archivo y pegarlo en otra ubicación.