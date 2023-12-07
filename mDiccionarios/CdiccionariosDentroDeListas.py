#Esta forma de almacenar datos, permite simular el almacenaje de objetos.

contactos: list = [
    {
        "nombre": "Daniel",
        "correo": "daniel@falso.local"
    },
    {
        "nombre": "Esteban",
        "correo": "esteban@falso.local"
    },
    {
        "nombre": "Andy",
        "correo": "andy@falso.local"
    } 
]

print(contactos[0]["nombre"])
print(contactos[1]["correo"])

print("******************************************")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Nombre del contacto: {contacto['correo']}")
    print("------------------------------------------")