file = open("arquivos/teste.txt", "r")
linhas = file.read().split("\n")

print(linhas)
for linha in linhas:
    nome, idade, endereco = linha.split(",")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Endereço: {endereco}")
    print("#"*50)   