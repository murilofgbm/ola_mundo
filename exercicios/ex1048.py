salario = round(float(input()), 2)
if 0 < salario <= 400:
    reajuste = 15
if 400 < salario <= 800:
    reajuste = 12
if 800 < salario <= 1200:
    reajuste = 10
if 1200 < salario <= 2000:
    reajuste = 7
if salario > 2000:
    reajuste = 4
novo_salario = salario*(reajuste/100+1)
reajuste_ganho = novo_salario-salario

print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste_ganho:.2f}")
print(f"Em percentual: {reajuste} %")
