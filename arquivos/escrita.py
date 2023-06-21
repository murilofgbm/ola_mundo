nome = input("")

file = open("arquivos/teste.txt", "w") #write
file.write(nome)
file.close()

