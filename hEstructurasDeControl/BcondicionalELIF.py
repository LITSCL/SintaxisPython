numero_1: int = 13
numero_2: int = 12
numero_3: int = 11
numero_4: int = 10

if (numero_1 < numero_4): #Se evalua la primera condición.
    print("La primera condicion se cumple") #Si la condición se cumplió, se ejecuta el código y se ignoran las demas condiciones, de no ser así, se procede a evaluar la próxima condición.
elif (numero_1 < numero_3):
    print("La segunda condicion se cumple")
elif (numero_1 < numero_2):
    print("La tercera condicion se cumple")
else:
    print("Ninguna condicion se cumplio") #Si ninguna condición se cumplió, se ejecuta esta instucción.