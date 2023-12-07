#MODULOS PROPIOS.
from nModulos import primer_modulo #Importando todas las funciones del modulo "primer_modulo" (Se necesita usar el modulo).
from nModulos.segundo_modulo import multiplicar #Importando la función "multiplicar" del modulo "segundo_modulo" (No se necesita usar el modulo).
from nModulos.tercer_modulo import * #Importando todas las funciones del modulo "tercer_modulo". (No se necesita usar el modulo).

#import primer_modulo #Importando todas las funciones del modulo "primer_modulo" (Se necesita usar el modulo).
#from segundo_modulo import multiplicar #Importando la función "multiplicar" del modulo "segundo_modulo" (No se necesita usar el modulo).
#from tercer_modulo import * #Importando todas las funciones del modulo "tercer_modulo". (No se necesita usar el modulo).

#MODULOS DE TERCEROS.
import datetime
import math
import random

print("---------Uso de modulos propios---------")

print(primer_modulo.sumar(3, 5))
print(primer_modulo.restar(5, 3))

print(multiplicar(3, 5)) 

print(decir_hola_mundo())
print(decir_chao_mundo())

print("---------Uso de modulos de terceros (DateTime)---------")

print(datetime.datetime.now().strftime("%d/%m/%Y"))
print(datetime.datetime.now().strftime("%d/%m/%Y | %H:%M:%S"))
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)

print("---------Uso de modulos de terceros (Math)---------")

print(math.sqrt(25)) #La función "sqrt" retorna la raíz cuadrada del número entregado por parámetro.
print(math.ceil(1.5)) #La función "ceil" redondea un numero hacia arriba.
print(math.floor(1.5)) #La función "floor" redondea un numero hacia abajo.

print("---------Uso de modulos de terceros (Random)---------")
print(random.randint(15, 65)) #La función "randint" permite calcular un número aleatorio entre los 2 parámetros entregados.