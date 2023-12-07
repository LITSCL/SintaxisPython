def primera_funcion():
    return "Retorno de la primera función"

def segunda_funcion():
    return "Retorno de la segunda función"

def funcion_maestra(): #Esta función ejecuta otras funciones en su bloque de instrucciones.
    variable = ""
    variable+=primera_funcion() + "\n"
    variable+=segunda_funcion()
    
    return variable
    
print(funcion_maestra()) #Imprimiendo el valor que retorna la función "funcion_maestra".
    