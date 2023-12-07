from _io import open
import pathlib

rutaAbsoluta: str = str(pathlib.Path().absolute())

#1. Abriendo el archivo (Permite trabajar con él).
archivo: object = open(rutaAbsoluta + "/01-archivo.txt", "r")

#2. Leyendo el archivo (Se almacena todo el conenido en la variable).
contenido: str = archivo.read()

#3. Mostrando el contenido del archivo.
print(contenido)
 
#4. Cerrando el archivo.
archivo.close()