class Calculadora():
    def soma(self, a,b):
        return a + b

    def sub(self, a,b):
        return a-b

    def mult(self, a,b):
        return a * b

    def div(self, a,b):
        if b == 0:
            print("Não é possível realizar divisçao por 0.")
            return("-1")
        else:
            return(a/b)



