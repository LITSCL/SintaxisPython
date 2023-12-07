import pathlib
import shutil

rutaOrigen: str = str(pathlib.Path().absolute()) + "/02-E.txt"
rutaDestino: str = str(pathlib.Path().absolute()) + "/EcopiarUnArchivo/02-E_copia.txt"

#Copiar y pegar archivo.
shutil.copyfile(rutaOrigen, rutaDestino) #La función "copyfile", permite copiar un archivo y pegarlo en otra ubicación.