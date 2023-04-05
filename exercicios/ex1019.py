duracao = int(input())
horas = duracao // 3600
resto_horas = duracao % 3600
minutos = resto_horas // 60
resto_minutos = resto_horas % 60
segundos = resto_minutos

print(f"{horas}:{minutos}:{segundos}")