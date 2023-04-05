tempo = int(input())
velocidade = int(input())
distancia = velocidade*tempo
autonomia = 12
litros = distancia/autonomia
print(f"{litros:.3f}")