class Cidade:
    def __init__(self, nome, distanciaObjetivo):
        self.nome = nome
        self.visitado = False
        self.distanciaObjetivo = distanciaObjetivo
        self.adjacentes = []

    def addCidadeAdjacente(self, cidade):
        self.adjacentes.append(cidade)


'''testes iniciais da classe
c = cidade("Teste")
print(c.nome)
print(c.visitado)'''
