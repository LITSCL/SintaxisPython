class Persona:
    __nombre: str = None
    __apellido: str = None
    __altura: str = None
    __edad: int = None

    def get_nombre(self) -> str:
        return self.__nombre

    def get_apellido(self) -> str:
        return self.__apellido

    def get_altura(self) -> str:
        return self.__altura

    def get_edad(self) -> int:
        return self.__edad

    def set_nombre(self, nombre: str):
        self.__nombre = nombre

    def set_apellido(self, apellido: str):
        self.__apellido = apellido

    def set_altura(self, altura: str):
        self.__altura = altura

    def set_edad(self, edad: int):
        self.__edad = edad
    
    def hablar(self) -> str:
        return "Estoy hablando"
    
    def caminar(self) -> str:
        return "Estoy caminando"
    