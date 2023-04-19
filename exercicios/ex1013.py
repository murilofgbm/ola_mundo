linha = input().split()
a = int(linha[0])
b = int(linha[1])
c = int(linha[2])
valor = int()

if a>=b and a>=c: 
    valor = a
if b>=a and b>=c:
    valor = b
if c>=a and c>=b:
    valor = c

print(f"{valor} eh o maior")
#and é uma adicao das proposicoes