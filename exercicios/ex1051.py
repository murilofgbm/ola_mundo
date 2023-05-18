salario = round(float(input()), 2)

if 0 <= salario <= 2000:
    print("Isento")
if 2000.01 <= salario <= 3000:
    renda = salario - 2000
    imposto = renda * 0.08
    print(f"R$ {imposto:.2f}")
if 3000.01 <= salario <= 4500:
    renda1 = 1000
    renda2 = salario - 3000
    imposto = (renda1*0.08)+(renda2*0.18)
    print(f"R$ {imposto:.2f}")
if salario > 4500.00:
    renda1 = 1000
    renda2 = 1500
    renda3 = salario - 4500
    imposto = (renda1*0.08)+(renda2*0.18)+(renda3*0.28)
    print(f"R$ {imposto:.2f}")