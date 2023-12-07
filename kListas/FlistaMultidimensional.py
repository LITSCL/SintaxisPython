#Las listas multidimensionales son aquellas que albergan listas en sus indices.

#Creando lista multidimensional.
contactos: list = [
    [
        "Daniel",
        "daniel@falso.local"
    ],
    [
        "Esteban",
        "esteban@falso.local"
    ],
    [
        "Andy",
        "andy@falso.local"  
    ]
]

print("---Imprimiendo [0][0]---")

print(contactos[0][0])

print("---Recoriendo con bucle for anidado---")

for i in contactos:
    for j in i:
        print(j)