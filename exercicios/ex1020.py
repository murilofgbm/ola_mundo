idade_dias= int(input())
anos = idade_dias // 365
resto_anos = idade_dias % 365
meses = resto_anos // 30
resto_meses = resto_anos % 30
dias = resto_meses

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")