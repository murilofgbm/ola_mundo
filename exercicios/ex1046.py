linha = input().split()
hora_inicial = int(linha[0])
hora_final = int(linha[1])

if hora_final == hora_inicial:
    duracao = 24
if hora_final < hora_inicial:
    duracao = (hora_final+24) - hora_inicial
if hora_final > hora_inicial:
    duracao = hora_final - hora_inicial

print(f"O JOGO DUROU {duracao} HORA(S)")    
