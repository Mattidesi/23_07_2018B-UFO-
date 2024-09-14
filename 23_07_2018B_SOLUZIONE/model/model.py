import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo=nx.Graph()
        self.lista_nodi=[]
        self.idMap={}


    def buildGraph(self, giorni, anno):
        self.grafo.clear()
        self.lista_nodi=DAO.getAllNodes()
        for nodo in self.lista_nodi:
            self.idMap[nodo.id]=nodo

        self.grafo.add_nodes_from(self.lista_nodi)
        vicini=DAO.getAllEdges()
        for s1, s2 in vicini:
            self.grafo.add_edge(self.idMap[s1], self.idMap[s2], weight=DAO.calcolaPeso(s1, s2, giorni, anno))

    def getNumNodes(self):
        return len(self.grafo.nodes)


    def getNumEdges(self):
        return len(self.grafo.edges)