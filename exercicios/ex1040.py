linha1 = input().split()
N1 = float(linha1[0])
N2 = float(linha1[1])
N3 = float(linha1[2])
N4 = float(linha1[3])

media = ((N1*2) + (N2*3) + (N3*4) + N4)/10
print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")

if media < 5.0:
    print("Aluno reprovado.")

if 5.0 <= media < 7:
    print("Aluno em exame.")
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    media_final = (media + nota_exame)/2
    if media_final >= 5:
        print("Aluno aprovado.")
    if media_final < 5:
        print("Aluno reprovado.")
    print(f"Media final: {media_final:.1f}")