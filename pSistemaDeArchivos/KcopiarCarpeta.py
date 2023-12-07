import pathlib
import shutil

rutaOrigen: str = str(pathlib.Path().absolute()) + "/mi_carpeta"
rutaDestino: str = str(pathlib.Path().absolute()) + "/mi_carpeta_copia"

#Copiar y pegar una carpeta.
shutil.copytree(rutaOrigen, rutaDestino) #La función "copytree", permite copiar una carpeta y pegarla en otra ubicación.