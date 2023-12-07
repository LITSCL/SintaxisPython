import pathlib
import os

rutaCarpeta: str = str(pathlib.Path().absolute()) + "/LlistarContenidoDeUnaCarpeta"

contenido: list = os.listdir(rutaCarpeta) #La función "listdir", recibe como parámetro la ruta de la carpeta y retorna una lista con el nombre de todos los archivos.

print(contenido)