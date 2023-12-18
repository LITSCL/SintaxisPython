import pathlib
import shutil

ruta_origen: str = str(pathlib.Path().absolute()) + "/03-F.txt"
ruta_destino: str = str(pathlib.Path().absolute()) + "/FmoverUnArchivo/03-F.txt"

#Cortar y pegar archivo.
shutil.move(ruta_origen, ruta_destino) #La función "move", permite cortar un archivo y pegarlo en otra ubicación.