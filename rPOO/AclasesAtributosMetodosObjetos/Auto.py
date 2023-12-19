#Una clase es un molde, en la cual se definen sus atributos y métodos.

class Auto:
    #Atributos de la clase.
    color: str = "Rojo"
    marca: str = "Ferrari"
    modelo: str = "Aventador"
    velocidad_actual: int = 0
    
    #Métodos Getters y Setters.
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
    
    #Métodos de la clase.
    def acelerar(self) -> None:
        self.velocidad_actual+=1

    def desacelerar(self) -> None:
        self.velocidad_actual-=1
        
#Creando un objeto de tipo "Auto".
auto: Auto = Auto()

print("----------Accediendo directamente al atributo----------")
print(auto.color)
print(auto.marca)
print(auto.modelo)
print(auto.velocidad_actual)

print("----------Accediendo al atributo mediante Getters----------")
print(auto.get_color())
print(auto.get_marca())
print(auto.get_modelo())
print(auto.get_velocidad_actual())

print("----------Modificando directamente el atributo----------")
auto.color = "Amarillo"
auto.marca = "Chevrolet"
auto.modelo = "Sail Sedan"
auto.velocidad_actual = 100

print(auto.color)
print(auto.marca)
print(auto.modelo)
print(auto.velocidad_actual)

print("----------Modificando el atributo mediante Setters----------")
auto.set_color("Verde")
auto.set_marca("Tesla")
auto.set_modelo("Model V")
auto.set_velocidad_actual(70)

print(auto.get_color())
print(auto.get_marca())
print(auto.get_modelo())
print(auto.get_velocidad_actual())