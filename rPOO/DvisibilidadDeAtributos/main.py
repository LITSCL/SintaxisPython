from rPOO.DvisibilidadDeAtributos.Auto import Auto

auto: Auto = Auto()

print(auto.propiedad_publica)
#print(auto.__propiedad_privada) #Esto no funciona, una propiedad privada solo es accesible desde un método.

print(auto.get_propiedad_privada())