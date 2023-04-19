linha = input().split()
hora_inicial = int(linha[0])
minuto_inicial = int(linha[1])
hora_final = int(linha[2])
minuto_final = int(linha[3])
hora = int()
minuto = int()

if hora_final == hora_inicial and minuto_inicial == minuto_final:
    hora = 24
    minuto = 0

if hora_final == hora_inicial and minuto_final < minuto_inicial:
    hora = 23
    minuto = (minuto_final+60) - minuto_inicial

if hora_final == hora_inicial and minuto_final > minuto_inicial:
    hora = 0
    minuto = minuto_final - minuto_inicial

if hora_final < hora_inicial and minuto_final > minuto_inicial:
    hora = (hora_final+24) - hora_inicial
    minuto = minuto_final - minuto_inicial

if hora_final > hora_inicial and minuto_final < minuto_inicial:
    hora = hora = (hora_final - hora_inicial) - 1
    minuto = (minuto_final+60) - minuto_inicial

if  hora_final < hora_inicial and minuto_final < minuto_inicial:
    hora = ((hora_final+24) - hora_inicial) - 1
    minuto = minuto = (minuto_final+60) - minuto_inicial

if hora_final > hora_inicial and minuto_final > minuto_inicial:
    hora = hora_final - hora_inicial
    minuto = minuto_final - minuto_inicial

if hora_final > hora_inicial and minuto_final == minuto_inicial:
    hora = hora_final - hora_inicial
    minuto = 0

if hora_final < hora_inicial and minuto_final == minuto_inicial:
    hora = (hora_final+24) - hora_inicial
    minuto = 0

    
print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")    
