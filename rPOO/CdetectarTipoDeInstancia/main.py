from rPOO.CdetectarTipoDeInstancia.Auto import Auto

auto: Auto = Auto("Rojo", "Ferrari", "Aventador", 0)

if (type(auto) == Auto):
    print("Es un objeto de tipo 'Auto'")
else:
    print("No es un objeto de tipo 'Auto'")



