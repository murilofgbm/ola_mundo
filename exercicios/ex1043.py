linha = input().split()
A = float(linha[0])
B = float(linha[1])
C = float(linha[2])

perimetro = A+B+C
area = ((A+B)*C)/2

if A < (B+C) and B < (A+C) and C < (A+B):
    print(f"Perimetro = {perimetro}")
else:
    print(f"Area = {area}")
