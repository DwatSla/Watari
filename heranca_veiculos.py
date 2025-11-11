class Veiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo


class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)
        self.__numero_portas = numero_portas

    def get_numero_portas(self):
        return self.__numero_portas

    def set_numero_portas(self, numero_portas):
        self.__numero_portas = numero_portas

