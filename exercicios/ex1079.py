quantidade = int(input())

class Media_ponderada():
    def __init__(self, nota1, nota2, nota3):
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def media(self):
        media = ((self.nota1*2) + (self.nota2*3) + (self.nota3*5))/10
        return media

medias_ponderadas = []

for i in range(quantidade):
    caso = input().split()
    nota1 = float(caso[0])
    nota2 = float(caso[1])
    nota3 = float(caso[2])

    caso_atual = Media_ponderada(nota1, nota2, nota3)
    media_ponderada = caso_atual.media()
    medias_ponderadas.append(media_ponderada)

for media in medias_ponderadas:
    print("{:.1f}".format(media))
