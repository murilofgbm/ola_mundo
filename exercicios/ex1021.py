N = int(float(input()) * 100)

notas100 = N // 10000
resto100 = N % 10000
notas50 = resto100 // 5000
resto50 = resto100 % 5000
notas20 = resto50 // 2000
resto20 = resto50 % 2000
notas10 = resto20 // 1000
resto10 = resto20 % 1000
notas5 = resto10 // 500
resto5 = resto10 % 500
notas2 = resto5 // 200
resto2 = resto5 % 200
moeda100 = resto2 // 100
restom100 = resto2 % 100
moeda50 = restom100 // 50
restom50 = restom100 % 50
moeda25 = restom50 // 25
restom25 = restom50 % 25
moeda10 = restom25 // 10
restom10 = restom25 % 10
moeda5 = restom10 // 5
restom5 = restom10 % 5
moeda1 = restom5 // 1

if 0 <= N <= 100000000:
    print("NOTAS:")
    print(f"{notas100} nota(s) de R$ 100.00")
    print(f"{notas50} nota(s) de R$ 50.00")
    print(f"{notas20} nota(s) de R$ 20.00")
    print(f"{notas10} nota(s) de R$ 10.00")
    print(f"{notas5} nota(s) de R$ 5.00")
    print(f"{notas2} nota(s) de R$ 2.00")
    
    print("MOEDAS:")
    print(f"{moeda100} moeda(s) de R$ 1.00")
    print(f"{moeda50} moeda(s) de R$ 0.50")
    print(f"{moeda25} moeda(s) de R$ 0.25")
    print(f"{moeda10} moeda(s) de R$ 0.10")
    print(f"{moeda5} moeda(s) de R$ 0.05")
    print(f"{moeda1} moeda(s) de R$ 0.01")