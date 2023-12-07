#Las funciones Lambda son funciones sencillas, las cuales pueden recibir parámetros o no, la ventaja que tienen es que pueden ser almacenadas en variabes (Funciones sin nombre).

#1. Creando función lambda sin parámetros.
retornar_el_mes = lambda : "El mes es Septiembre"

#2. Creando función lambda con un parámetro.
retornar_el_dia = lambda dia: f"El día es {dia}"

#3. Creando función lambda con dos parámetros.
retornar_la_suma = lambda numero_1, numero_2: numero_1 + numero_2

print(retornar_el_mes())
print(retornar_el_dia("Viernes"))
print(retornar_la_suma(1, 2))
