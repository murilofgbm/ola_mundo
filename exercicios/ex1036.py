linha = input().split()
A = float(linha[0])
B = float(linha[1])
C = float(linha[2])
delta = B*B - 4*A*C
if delta < 0 or A == 0:
    print("Impossivel calcular")
else:
    raiz1 = (B*-1 + delta**(1/2))/(2*A)
    raiz2 = (B*-1 - delta**(1/2))/(2*A)
    print(f"R1 = {raiz1:.5f}")
    print(f"R2 = {raiz2:.5f}")