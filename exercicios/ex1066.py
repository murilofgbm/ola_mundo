def classificar_numeros():
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0

    for i in range(5):
        numero = int(input())
        if numero % 2 == 0:
            pares += 1
        if numero > 0:
            positivos += 1
        if numero < 0:
            negativos += 1
        if numero % 2 != 0:
            impares += 1
    return pares, impares, positivos, negativos

quantidade_pares, quantidade_impares, quantidade_positivos, quantidade_negativos = classificar_numeros()
print(f"{quantidade_pares} valor(es) par(es)")
print(f"{quantidade_impares} valor(es) impar(es)")
print(f"{quantidade_positivos} valor(es) positivo(s)")
print(f"{quantidade_negativos} valor(es) negativo(s)")
