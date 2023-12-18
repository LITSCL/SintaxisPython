import pathlib
import os

ruta_carpeta: str = str(pathlib.Path().absolute()) + "/LlistarContenidoDeUnaCarpeta"

contenido: list = os.listdir(ruta_carpeta) #La función "listdir", recibe como parámetro la ruta de la carpeta y retorna una lista con el nombre de todos los archivos.

print(contenido)