#El tipo de dato "set", es similar a una lista pero no tiene indices ni ningún tipo de orden.

peliculas: set = {"Django", "Ponyo", "Terminator"}

peliculas.add("Alien") #La función "add" permite añadir un elemento al set (Se agrega en cualquier orden).
peliculas.add("Alien") #No se agregan datos repetidos.
peliculas.add("Alien") #No se agregan datos repetidos.

print(peliculas)

peliculas.remove("Alien")

print(peliculas)




