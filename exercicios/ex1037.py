valor = float(input())

if 0 <= valor <= 25.00:
    print("Intervalo [0,25]")
if 25 < valor <= 50.00:
    print("Intervalo (25,50]")
if 50 < valor <= 75.00:
    print("Intervalo (50,75]")
if 75 < valor <= 100:
    print("Intervalo (75,100]")
if valor < 0 or valor > 100:
    print("Fora de intervalo")

