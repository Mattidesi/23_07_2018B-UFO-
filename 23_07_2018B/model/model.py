import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.nodes = []
        self.grafo = nx.Graph()
        self.idMap = {}

    def getYears(self):
        return DAO.getYears()

    def buildGraph(self,year,gg):
        self.nodes = DAO.getAllNodes()
        self.grafo.add_nodes_from(self.nodes)

        for node in self.nodes:
            self.idMap[node.id] = node

        edges = DAO.getAllEdges(self.idMap)

        for edge in edges:
            if self.grafo.has_edge(edge.s1,edge.s2):
                return
            else:
                self.grafo.add_edge(edge.s1,edge.s2,weight = DAO.getAllWeight(edge.s1.id,edge.s2.id,year,gg))


    def getSumWeightNeighbor(self):
        result = []

        for node in self.grafo:
            score = 0
            for v in self.grafo.neighbors(node):
                score += self.grafo[node][v]['weight']
            result.append((node,score))

        return result
    def getGraphDetails(self):
        return len(self.grafo.nodes), len(self.grafo.edges)