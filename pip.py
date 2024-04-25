class Animal:
    def __init__(self, nome):
        self.nome
    def fazer_som(self):
        print("O animal faz algum som")
class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def fazer_som(som):
         print("O cachorro faz au au!")
