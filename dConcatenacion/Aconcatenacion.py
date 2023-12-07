string_1: str = "Hola"
string_2: str = "Soy"
string_3: str = "Daniel"

#Concatenacion 1.
print("Forma 1:")
print(string_1 + " " + string_2 + " " + string_3)

print("")

#Concatenacion 2.
print("Forma 2:")
print(string_1, string_2, string_3)

print("")

#Concatenacion 3.
print("Forma 3:")
print(f"{string_1} {string_2} {string_3}")

print("")

#Concatenacion 4.
print("Forma 4:")
print("{} {} {}".format(string_1, string_2, string_3)) #El metodo "format" se aplica a una cadena, donde cada parametro entregado reemplaza a los corchetes (Se reemplazan en orden).