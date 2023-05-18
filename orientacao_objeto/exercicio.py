class Carro():
    def __init__(self, nome, modelo, cor, ano):
        self.nome = nome
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    
    def print(self):
        print(f"O nome do carro é {self.nome} do modelo {self.modelo}, na cor {self.cor} do ano de {self.ano}")

    def buzina(self):
        print("Buzinaa!")

carro1 = Carro("Mustang", "GT", "vermelho", 2023)
carro1.print()
carro1.buzina()