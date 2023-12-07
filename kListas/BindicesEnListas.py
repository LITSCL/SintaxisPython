peliculas: list = ["Django", "Ponyo", "Terminator", "Alien"]

print("---Indices Positivos---")

#Accediendo a datos utilizando indices positivos (Desde el primer dato hacia el último).
print(peliculas[0])
print(peliculas[1])
print(peliculas[2])
print(peliculas[3])

print("---Indices Negativos---")

#Accediendo a datos utilizando indices negativos (Desde el último dato hacia el primero).
print(peliculas[-1])
print(peliculas[-2])
print(peliculas[-3])
print(peliculas[-4])

print("---Rango de Indices 1---")

print(peliculas[1:3]) #Indicando que se quiere obtener una lista desde el indice 1 hasta el indice 3 (Excluyendolo).

print("---Rango de Indices 2---")

print(peliculas[1:]) #Indicando que se quiere obtener una lista desde el indice 1 hasta el último indice.