from Mapa import Mapa
from Pilha import Pilha


class Profundidade:
    def __init__(self, inicio, objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        self.fronteira = Pilha(20)
        self.fronteira.empilhar(inicio)

    def buscar(self):
        topo = self.fronteira.getTopo()
        print("Topo: {}".format(topo.nome))  # type: ignore

        for a in topo.adjacentes:  # type: ignore
            print("Verificando se {} já foi visitado".format(a.cidade.nome))
            if a.cidade.visitado == False:
                a.cidade.visitado = True
                self.fronteira.empilhar(a.cidade)
                Profundidade.buscar(self)
        print("Desempilhando {}".format(
            self.fronteira.desempilhar().nome))  # type: ignore


mapa = Mapa()
profundidade = Profundidade(mapa.portoUniao, mapa.curitiba)
profundidade.buscar()
