def contar_positivos():
    positivos = int()
    soma = float()
    for i in range(6):
        numero = float(input())
        if numero > 0:
            positivos = positivos + 1
            soma = soma + numero
    return positivos, soma



def calcular_media(soma, positivos):
    media_total = (soma / positivos)
    return media_total

quantidade_positivos, soma_positivos = contar_positivos()
media_positivos = calcular_media(soma_positivos, quantidade_positivos)

print(f"{quantidade_positivos} valores positivos")
print(f"{media_positivos:.1f}")