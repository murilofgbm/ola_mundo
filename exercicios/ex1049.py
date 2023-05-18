vertebra = input()
tipo = input()
alimento = input()

if vertebra == "vertebrado":
    if tipo == "ave":
        if alimento == "carnivoro":
            print("aguia")
        if alimento == "onivoro":
            print("pomba")
    if tipo == "mamifero":
        if alimento == "onivoro":
            print("homem")
        if alimento == "herbivoro":
            print("vaca")
if vertebra == "invertebrado":
    if tipo == "inseto":
        if alimento == "hematofago":
            print("pulga")
        if alimento == "herbivoro":
            print("lagarta")
    if tipo == "anelideo":
        if alimento == "hematofago":
            print("sanguessuga")
        if alimento == "onivoro":
            print("minhoca")
