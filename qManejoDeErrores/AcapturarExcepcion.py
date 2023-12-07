numero_1: int = 5
numero_2: int = 0

print("---ZeroDivisionError---")
try: #La cláusula "try", intenta ejecutar todo el código en el bloque.
    print(numero_1 / numero_2)
except: #La cláusula "except", se ejecuta si ocurrió un error en la cláusula "try".
    print("A ocurrido un error")
finally:
    print("Este mensaje siempre se envía, pase lo que pase") #La cláusula "finally", siempre se ejecua, ocurra o no un error.
    