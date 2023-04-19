N = int(input())
i = 0

while i < N < 10000:
    X = int(input())
    if X % 2 == 0 and X > 0:
        print("EVEN POSITIVE")
    if X % 2 == 0 and X < 0:
        print("EVEN NEGATIVE")
    if X % 2 != 0 and X > 0:
        print("ODD POSITIVE")
    if X % 2 != 0 and X < 0:
        print("ODD NEGATIVE")
    if X == 0:
        print("NULL")
    i = i + 1
    