N = int(input())
i = 1


while i <= N and 5 < N < 2000:
    if i % 2 == 0:
        quadrado = i*i
        print (f"{i}^2 = {quadrado}")
    i = i + 1