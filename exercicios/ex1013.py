linha = input().split()
a = int(linha[0])
b = int(linha[1])
c = int(linha[2])

if a>b and a>c: 
    print(f"{a} eh o maior")
if b>a and b>c:
    print(f"{b} eh o maior")
if c>a and c>b:
    print(f"{c} eh o maior")
#and é uma adicao das proposicoes