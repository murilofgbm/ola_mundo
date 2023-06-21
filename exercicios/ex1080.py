class Maior():
    def __init__(self, lista):
        self.lista = lista

    def verificar(self):
        maior = max(self.lista)
        posicao = self.lista.index(maior) + 1
        print(maior)
        print(posicao)

lista1 = []

for i in range(100):
    numero = int(input())
    lista1.append(numero)

lista1 = Maior(lista1)
lista1.verificar()