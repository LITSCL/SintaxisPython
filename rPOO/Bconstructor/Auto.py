class Auto:
    #1. Atributos de la clase.
    color: str = None
    marca: str = None
    modelo: str = None
    velocidad_actual: int = None
    
    #2. Constructor de la clase (Permite entregar los atributos al momento de crear una instancia).
    def __init__(self, color: str, marca: str, modelo: str, velocidad_actual: int) -> None:
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad_actual = velocidad_actual
    
    #3. Métodos Getters y Setters.
    def get_color(self) -> str:
        return self.color

    def get_marca(self) -> str:
        return self.marca

    def get_modelo(self) -> str:
        return self.modelo

    def get_velocidad_actual(self) -> int:
        return self.velocidad_actual

    def set_color(self, color: str) -> None:
        self.color = color

    def set_marca(self, marca: str) -> None:
        self.marca = marca

    def set_modelo(self, modelo: str) -> None:
        self.modelo = modelo

    def set_velocidad_actual(self, velocidad_actual: int) -> None:
        self.velocidad_actual = velocidad_actual
        
    def to_string(self) -> str:
        string: str = "Color: " + self.get_color() + "\n"
        string+="Marca: " + self.get_marca() + "\n"
        string+="Modelo: " + self.get_modelo() + "\n"
        string+="VelocidadActual: " + str(self.get_velocidad_actual()) + "\n"
        
        return string
    
    #4. Métodos de la clase.
    def acelerar(self) -> None:
        self.velocidad_actual+=1

    def desacelerar(self) -> None:
        self.velocidad_actual-=1