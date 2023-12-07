#Declarando la función con un parámetro.
def mostrar_nombre(nombre: str) -> None:
    print(nombre)

#Llamando la función y entregando un parámetro.
mostrar_nombre("Daniel")

#--------------------------------------------------------------------------------------------

#Declarando la función con dos parámetros.
def mostrar_nombre_mas_apellido(nombre: str, apellido: str) -> None:
    print(nombre + " " + apellido)

#Llamando la función y entregando dos parámetros.
mostrar_nombre_mas_apellido("Daniel", "Alvarez")