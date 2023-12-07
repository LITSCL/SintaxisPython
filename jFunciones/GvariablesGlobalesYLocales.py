#Variable Global: Es una variable que al ser declarada e inciciada puede ser accedida desde cualquier estructura del programa.
#Variable Local: Es una variable que al ser declarada e inciciada puede ser accedida únicamente dentro de la estructura en la que se encuentra.


#1. Ejemplo de uso de una variable global (Toda variable fuera de un bloque es global).
variable_1 = "Variable 1"

def retornar_variable_global():
    return variable_1

print(variable_1) #Accediendo a la variable (Exitoso).

#2. Ejemplo de uso de una variable local (Toda variable dentro de un bloque es local).
def retornar_variable_local():
    variable_2 = "Variable 2"
    return variable_2

#print(variable_2) #Accediendo a la variable (Fallido).
print("Error")


#3. Ejemplo de uso de una variable global.
def retornar_variable_global_ejecutada():
    global variable_3 #Declarando variable global (Si se desea que una variable dentro de un bloque sea global, esto se debe especificar).
    variable_3 = "Variable 3" #Iniciando variable global.
    return variable_3

retornar_variable_global_ejecutada() #Una variable local declarada dentro de un bloque solo puede ser utilizada desde afuera cuando ya se ejecutó dicho bloque.
print(variable_3) #Accediendo a la variable (Exitoso).
