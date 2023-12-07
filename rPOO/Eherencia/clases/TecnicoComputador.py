from rPOO.Eherencia.clases.Informatico import Informatico

#La herencia permite a una clase hija, heredar todos los atributos y métodos de una clase padre.

class TecnicoComputador(Informatico): #La clase "TecnicoComputador" está heredando de la clase "Informatico" (Padre = Persona | Hija = Informatico).
    __certificados: list = None
    
    def __init__(self) -> None:
        super().__init__() #Indica que al momento de crear una instancia de "TecnicoComputador", también se ejecuta el contructor de la clase padre.
        self.__certificados = ["Cisco", "Microsoft"]

    def get_certificados(self) -> list:
        return self.__certificados

    def set_certificados(self, certificados: list) -> None:
        self.__certificados = certificados
    
    def formatear(self) -> str:
        return "Estoy formateando"  
    
    def instalar_programa(self) -> str:
        return "Estoy instalando un programa"