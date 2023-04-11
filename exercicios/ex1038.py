linha = input().split()
codigo = int(linha[0])
quantidade = int(linha[1])

if codigo == 1:
    total = quantidade * 4
if codigo == 2:
    total = quantidade * 4.5
if codigo == 3:
    total = quantidade * 5
if codigo == 4:
    total = quantidade * 2
if codigo == 5:
    total = quantidade * 1.5
print(f"Total: R$ {total:.2f}")