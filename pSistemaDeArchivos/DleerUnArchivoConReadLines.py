from _io import open
import pathlib

rutaAbsoluta: str = str(pathlib.Path().absolute())

#1. Abriendo el archivo (Permite trabajar con él).
archivo: object = open(rutaAbsoluta + "/01-archivo.txt", "r")

#2. Leyendo el archivo (Se almacena todo el conenido en la variable).
lista: list = archivo.readlines() #Esto es útil para obtener cada línea del archivo dentro de un indice de una lista.

#3. Mostrando el contenido del archivo.
for i in lista:
    print(i)
 
#4. Cerrando el archivo.
archivo.close()