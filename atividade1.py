class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def set_nome(self, nome):
        self.__nome = nome

    def set_idade(self, idade):
        self.__idade = idade

    def verificar_maioridade(self):
        if self.__idade >= 18:
            print(f"Olá, {self.__nome}, você é maior de idade.")
        else:
            print(f"Olá, {self.__nome}, você é menor de idade.")


nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))

pessoa = Pessoa(nome, idade)
pessoa.verificar_maioridade()
