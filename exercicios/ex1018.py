N = int(input())

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
notas1 = resto2 // 1
resto1 = resto2 % 1

if 0<N<1000000:
    print(N)
print(f"{notas100} nota(s) de R$ 100,00")
print(f"{notas50} nota(s) de R$ 50,00")
print(f"{notas20} nota(s) de R$ 20,00")
print(f"{notas10} nota(s) de R$ 10,00")
print(f"{notas5} nota(s) de R$ 5,00")
print(f"{notas2} nota(s) de R$ 2,00")
print(f"{notas1} nota(s) de R$ 1,00")