class Numero():
    def __init__(self, numero):
        self.numero = numero
        self.impar_1 = None
        self.impar_2 = None
        self.impar_3 = None
        self.impar_4 = None
        self.impar_5 = None
        self.impar_6 = None

    def impares_consecutivos(self):
        if self.numero % 2 == 0:
            self.impar_1 = self.numero + 1
            self.impar_2 = self.numero + 3
            self.impar_3 = self.numero + 5
            self.impar_4 = self.numero + 7
            self.impar_5 = self.numero + 9
            self.impar_6 = self.numero + 11
        else:
            self.impar_1 = self.numero
            self.impar_2 = self.numero + 2
            self.impar_3 = self.numero + 4
            self.impar_4 = self.numero + 6
            self.impar_5 = self.numero + 8
            self.impar_6 = self.numero + 10
            
    def print(self):
        print(self.impar_1)
        print(self.impar_2)
        print(self.impar_3)
        print(self.impar_4)
        print(self.impar_5)
        print(self.impar_6)


numero = int(input())
numero1 = Numero(numero)
numero1.impares_consecutivos()
numero1.print()