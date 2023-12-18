import pathlib
import shutil

ruta_origen: str = str(pathlib.Path().absolute()) + "/mi_carpeta"
ruta_destino: str = str(pathlib.Path().absolute()) + "/mi_carpeta_copia"

#Copiar y pegar una carpeta.
shutil.copytree(ruta_origen, ruta_destino) #La función "copytree", permite copiar una carpeta y pegarla en otra ubicación.