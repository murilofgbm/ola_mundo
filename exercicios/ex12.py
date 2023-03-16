peso  = float(input("Digite seu peso em kg: "))
altura  = float(input("Digite sua altura em m: "))
IMC = peso/(altura*altura)

if IMC <= 18.5:
    print("Abaixo do Peso")

if 18.5 < IMC <= 24.9:
    print("Saudável")

if 24.9 < IMC <= 29.9:
    print("Peso em excesso")

if 29.9 < IMC <= 34.9:
    print("Obesidade Grau I")

if 34.9 < IMC <= 39.9:
    print("Obesidade Grau II(severa)")

if IMC >= 40:
    print("Obesidade Grau III(morbida)")