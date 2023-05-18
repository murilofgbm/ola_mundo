class Ho():
    def __init__(self, numero):
        self.numero = numero

    def print(self):
        for i in range(self.numero - 1):
            print("Ho", end=" ")
        print("Ho!")

numero = int(input())

ho1 = Ho(numero)
ho1.print()
