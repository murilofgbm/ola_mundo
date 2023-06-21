class Tabuada():
    def __init__(self, numero):
        self.numero = numero
    def calcular(self):
        for i in range(1, 11):
            resultado = i * self.numero
            print(f"{i} x {self.numero} = {resultado}")

numero1 = int(input())
numero1 = Tabuada(numero1)
numero1.calcular()
