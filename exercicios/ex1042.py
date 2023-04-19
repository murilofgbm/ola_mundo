linha = input().split()
a = int(linha[0])
b = int(linha[1])
c = int(linha[2])

if a<b and a<c:
    print(a)
    if b<c:
        print(b)
        print(c)
    if c<b:
        print(c)
        print(b)

if b<a and b<c:
    print(b)
    if a<c:
        print(a)
        print(c)
    if c<a:
        print(c)
        print(a)

if c<a and c<b:
    print(c)
    if a<b:
        print(a)
        print(b)
    if b<a:
        print(b)
        print(a)

print()
print(a)
print(b)
print(c)