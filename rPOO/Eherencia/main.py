from rPOO.Eherencia.clases.Persona import Persona
from rPOO.Eherencia.clases.Informatico import Informatico
from rPOO.Eherencia.clases.TecnicoComputador import TecnicoComputador

persona: Persona = Persona()

persona.set_nombre("Daniel")
persona.set_apellido("Alvarez")
persona.set_altura("180cm")
persona.set_edad(25)

informatico = Informatico() #La clase "Informatico" hereda de "Persona", por ende, se también posee sus atributos.

informatico.set_nombre("Esteban")
informatico.set_apellido("Alvarez")
informatico.set_altura("170cm")
informatico.set_edad(24)

tecnico_computador: TecnicoComputador = TecnicoComputador() #La clase "TecnicoComputador" hereda de "Informatico", por ende, se también posee sus atributos.

tecnico_computador.set_nombre("Angel")
tecnico_computador.set_apellido("Berrios")
tecnico_computador.set_altura("175cm")
tecnico_computador.set_edad(24)

print("----------------Persona----------------") #Clase padre (No hereda de ninguna otra clase).
print(f"La persona es: {persona.get_nombre()} {persona.get_apellido()}")
print(persona.hablar())
print("---------------------------------------")

print("--------------Informatico--------------") #Clase hija (Hereda de la clase "Persona").
print(f"El informatico es: {informatico.get_nombre()} {informatico.get_apellido()}")
print(informatico.get_lenguajes())
print(informatico.hablar()) #Este método es heredado.
print(informatico.programar())
print("---------------------------------------")

print("----------Tecnico Computador-----------") #Clase hija (Hereda de la clase "Informatico").
print(f"El tecnico es: {tecnico_computador.get_nombre()} {tecnico_computador.get_apellido()}")
print(tecnico_computador.get_lenguajes()) #Este método es heredado.
print(tecnico_computador.hablar()) #Este método es heredado.
print(tecnico_computador.programar()) #Este método es heredado.
print("---------------------------------------")
