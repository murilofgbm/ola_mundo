ponto = input().split()
X = round(float(ponto[0]), 1)
Y = round(float(ponto[1]), 1)

if X > 0 and Y > 0:
    print("Q1")
if X < 0 and Y > 0:
    print("Q2")
if X > 0 and Y < 0:
    print("Q4")
if X < 0 and Y < 0:
    print("Q3")
if X == 0 and Y == 0:
    print("Origem")
if X == 0 and Y != 0:
    print("Eixo Y")
if Y == 0 and X != 0:
    print("Eixo X")
