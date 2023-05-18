def contar_pares():
    pares = int()
    for i in range(5):
        numero = int(input())
        if numero % 2 == 0:
            pares = pares + 1
    print(f"{pares} valores pares")

contar_pares()