import pathlib
import shutil

rutaOrigen: str = str(pathlib.Path().absolute()) + "/03-F.txt"
rutaDestino: str = str(pathlib.Path().absolute()) + "/FmoverUnArchivo/03-F.txt"

#Cortar y pegar archivo.
shutil.move(rutaOrigen, rutaDestino) #La función "move", permite cortar un archivo y pegarlo en otra ubicación.