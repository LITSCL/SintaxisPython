numero_1: int = 10
numero_2: int = 15

#En Python solo se pueden concatenar str, asi que los datos se deben de refundir.
suma = numero_1 + numero_2
print("La suma de " + str(numero_1) + " con " + str(numero_2) + " es igual a: " + str(suma))
        
resta = numero_1 - numero_2
print("La resta de " + str(numero_1) + " con " + str(numero_2) + " es igual a: " + str(resta))
        
multiplicacion = numero_1 * numero_2
print("La multiplicacion de " + str(numero_1) + " con " + str(numero_2) + " es igual a: " + str(multiplicacion))
        
division = numero_1 / numero_2
print("La division de " + str(numero_1) + " con " + str(numero_2) + " es igual a: " + str(division))
        
modulo = numero_1 % numero_2
print("El modulo de " + str(numero_1) + " con " + str(numero_2) + " es igual a: " + str(modulo))