#Las funciones predefinidas son aquellas que vienen por defecto en Python.

#1. Función "isinstance".
print("---Función 'isinstance'---")
numero = 10
comprobacion = isinstance(numero, str) #La función "isinstance" recibe 2 parámetros, primero una variable y segundo un tipo de dato, si ambos parámetros pertenecen al mismo tipo de dato se retorna True, de lo contrario se retorna False.
print(comprobacion)
print("--------------------------")

print("")

#2. Función "strip".
print("---Función 'strip'---")
frase = "     Hola Mundo    "
print(frase)
print(frase.strip()) #La función "strip", se aplica a una cadena de texto y permite borrar los espacios que existen al comienzo y al final de la cadena.
print("--------------------------")

print("")

#3. Función "len".
print("---Función 'len'---")
texto = ""
if (len(texto) == 0): #La función "len", recibe como parámetro una cadena de texto, retorna la cantidad de caracteres.
    print("No hay texto en la variable")
print("--------------------------")

print("")

#4. Función "find".
print("---Función 'find'---")
cadena = "Necesito dinero por favor"
print(cadena.find("dinero")) #La función "find", se aplica a una cadena de texto, debe recibir como parametro una palabra, en caso de existir la palabra en la cadena se retorna el indice de la primera letra (De lo contrario retorna -1).
print("--------------------------")

print("")

#5. Función "replace".
print("---Función 'replace'---")
mi_texto = "Overlord es el mejor anime"
print(mi_texto.replace("Overlord", "SPY x FAMILY")) #La función "replace", se aplica a una cadena de texto y permite reemplazar una palabra, el primer parámetro es la palabra antigua y el segundo la nueva.
print("--------------------------")

print("")

#6. Función "lower".
print("---Función 'lower'---")
texto_mayusculas = "HOLA COMO ESTAS"
print(texto_mayusculas.lower()) #La función "lower", se aplica a una cadena de texto, permite convertir todo el texto a minusculas.
print("--------------------------")

print("")

#7. Función "upper".
print("---Función 'upper'---")
texto_minusculas = "hola como estas"
print(texto_minusculas.upper()) #La función "upper", se aplica a una cadena de texto, permite convertir todo el texto a mayusculas.
print("--------------------------")