from rPOO.Eherencia.clases.Persona import Persona

#La herencia permite a una clase hija, heredar todos los atributos y métodos de una clase padre.

class Informatico(Persona): #La clase "Informatico" está heredando de la clase "Persona" (Padre = Persona | Hija = Informatico).
    __lenguajes: list = None
    
    def __init__(self):
        self.__lenguajes = ["Java", "PHP", "JavaScript", "Python"]

    def get_lenguajes(self) -> list:
        return self.__lenguajes

    def set_lenguajes(self, lenguajes: list):
        self.__lenguajes = lenguajes
    
    def programar(self) -> str:
        return "Estoy programando"  
    
    def depurar(self) -> str:
        return "Estoy depurando"
        