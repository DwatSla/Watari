class Tabuada:
    def __init__(self, numero):
        self.__numero = numero

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def mostrar_tabuada(self):
        print(f"--- Tabuada do {self.__numero} ---")
        for i in range(1, 11):
            print(f"{self.__numero} x {i} = {self.__numero * i}")


numero = int(input("Digite um número para ver a tabuada: "))
tabuada = Tabuada(numero)
tabuada.mostrar_tabuada()
