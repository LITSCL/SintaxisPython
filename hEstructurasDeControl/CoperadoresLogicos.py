numero_1: int = 10
numero_2: int = -5

#Operador lógico and.
print("Operador logico and:")

if (numero_1 > 0 and numero_2 < 0):
    print("Ambas condiciones se cumplen") #Si ambas condiciones se cumplen se ejecuta la instrucción.
else:
    print("Una condicion o ambas no se estan cumpliendo")
        
print("")

#Operador lógico or.
print("Operador logico or:")

if (numero_1 > 0 or numero_2 < 0):
    print("Una o ambas condiciones se estan cumpliendo") #Con que una condición se cumpla se ejecuta la instrucción.
else:
    print("Ninguna condicion se esta cumpliendo")
        

