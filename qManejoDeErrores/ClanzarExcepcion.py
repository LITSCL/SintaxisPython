nombre: str = input("Introduce el nombre: ")
numero: int = 305

if (len(nombre) == 0):
    raise ValueError("El nombre no puede estar vacio") #La cláusula "raise" permite lanzar una excepción.

if (type(numero) != int):
    raise TypeError("El numero es un String")