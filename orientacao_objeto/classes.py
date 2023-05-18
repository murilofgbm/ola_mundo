class Pessoa():
    nome = ""
    idade = 0
    documento = ""

    def __init__(self, nome, idade, documento):
        self.nome = nome
        self.idade= idade
        self.documento = documento

    def print(self):
        print(f"O nome é {self.nome} a idade é {self.idade} e o documento é {self.documento}")


pessoa1 = Pessoa("Murilo", 15, "99999")
pessoa1.print()