class Auto:
    propiedad_publica: str = "Publico"
    __propiedad_privada: str = "Privado" #Una propiedad privada se declara utilizando 2 guiones bajos al principio de su nombre.
  
    def get_propiedad_publica(self) -> str:
        return self.__propiedad_publica

    def get_propiedad_privada(self) -> str:
        return self.__propiedad_privada

    def set_propiedad_publica(self, propiedad_publica: str) -> None:
        self.__propiedad_publica = propiedad_publica

    def set_propiedad_privada(self, propiedad_privada: str) -> None:
        self.__propiedad_privada = propiedad_privada
