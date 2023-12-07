numero_1: int = 0
numero_2: int = 20

print("Bucle while")
while (numero_1 < numero_2): #Repite mientras numero_1 sea menor que numero_2.
    
    if (numero_1 == 10):
        break #Al leer esta instrucción el programa se sale del bucle.
    
    print(numero_1)
    numero_1+=1
    
numero_1 = 0
numero_2 = 20
    
print("Bucle for")
for i in range(20): #Bucle for que repite 20 iteraciones.
    
    if (i == 10):
        break #Al leer esta instrucción el programa se sale del bucle.
    
    print(i)