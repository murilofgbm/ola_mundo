dicionario = {
    'nome': 'Murilo',
    'idade': '16'
}
dicionario['curso'] = "Ciencia da Computacao" #nova propriedade depois de ja declarado
dicionario['nome'] = "Pedro" # atualiza o valor
print(dicionario['nome'])
print(dicionario['idade'])
print(dicionario['curso'])
print(dicionario)

for key in dicionario.keys(): #imprime o nome da variavel
    if (key == 'nome'):
        print(f"O {key} é {dicionario[key]}")
    else:
        print(key, dicionario[key])