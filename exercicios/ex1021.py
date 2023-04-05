N = round(float(input()), 2)

notas100 = N // 100
resto100 = N % 100                      # // - so a parte inteira da divisao
notas50 = resto100 // 50                # % - o resto da divisao
resto50 = resto100 % 50
notas20 = resto50 // 20
resto20 = resto50 % 20
notas10 = resto20 // 10
resto10 = resto20 % 10
notas5 = resto10 // 5
resto5 = resto10 % 5
notas2 = resto5 // 2
resto2 = resto5 % 2
moeda100 = resto2 // 1
restom100 = resto2 % 1
moeda50 = restom100 // 0.50
restom50 = restom100 % 0.50
moeda25 = restom50 // 0.25
restom25 = restom50 % 0.25
moeda10 = restom25 // 0.10
restom10 = restom25 % 0.10
moeda5 = restom10 // 0.05
restom5 = restom10 % 0.05
moeda1 = restom5 // 0.01

if 0 <= N <= 1000000.00:
    print(f"NOTAS:") 
    print(f"{notas100:.0f} nota(s) de R$ 100.00")
    print(f"{notas50:.0f} nota(s) de R$ 50.00")
    print(f"{notas20:.0f} nota(s) de R$ 20.00")
    print(f"{notas10:.0f} nota(s) de R$ 10.00")
    print(f"{notas5:.0f} nota(s) de R$ 5.00")
    print(f"{notas2:.0f} nota(s) de R$ 2.00")

    print(f"MOEDAS:")
    print(f"{moeda100:.0f} moeda(s) de R$ 1.00")
    print(f"{moeda50:.0f} moeda(s) de R$ 0.50")
    print(f"{moeda25:.0f} moeda(s) de R$ 0.25")
    print(f"{moeda10:.0f} moeda(s) de R$ 0.10")
    print(f"{moeda5:.0f} moeda(s) de R$ 0.05")
    print(f"{moeda1:.0f} moeda(s) de R$ 0.01")