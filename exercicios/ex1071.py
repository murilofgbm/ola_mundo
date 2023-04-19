x = int(input())
y = int(input())

if x > y:
    aux = x     #trocar de posicao os valores
    x = y
    y = aux - 1 #menos 1 para nao incluir o cara no final


soma = 0
while x < y:  
    x = x + 1
    if x % 2 != 0:
        soma = soma + x

print(soma)