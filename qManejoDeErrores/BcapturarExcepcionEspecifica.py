try:
    numero: int = int(input("Ingresa un número para elevarlo al cuadrado: "))
    print("El cuadrado es: " + str(numero * numero))
except TypeError:
    print("TypeError: No se puede multiplicar un String")
except ValueError:
    print("ValueError: No puedes convertir caracteres a Int")
