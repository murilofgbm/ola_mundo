class Numero():
    def __init__(self, numero):
        self.numero = numero

    def resto_2(self):
        for i in range(1,10000):
            if i % self.numero == 2:
                print(i)


numero1 = int(input())

numero1 = Numero(numero1)
numero1.resto_2()