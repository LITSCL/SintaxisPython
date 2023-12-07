def mostrar_nombre(nombre: str = "Daniel") -> None: #Cuando se asigna un valor al parámetro, no es necesario entregarlo en la llamada.
    print(nombre)
    
mostrar_nombre() #Llamando la función sin entregar el parámetro.
mostrar_nombre("Nicolas") #Llamando la función entregando el parámetro.