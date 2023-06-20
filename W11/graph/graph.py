class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectTo = {}

    def addNeighbor(self, neighbor, weight=0):
        self.connectTo[neighbor] = weight

    def __str__(self):
        return str(self.id) + " connect to " + str([vtx.id for vtx in self.connectTo])

    def getConnections(self):
        return self.connectTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectTo[nbr]


class Graph:
    def __init__(self):
        self.vertexDic = {}
        self.numOfVertices = 0

    def addVertex(self, key):
        self.numOfVertices += 1
        new = Vertex(key)
        self.vertexDic[key] = new
        return new

    def getVertex(self, vtx):
        if vtx in self.vertexDic:
            return self.vertexDic[vtx]
        else:
            return None

    def __contains__(self, vtx):
        return vtx in self.vertexDic

    def addEdge(self, vtx1, vtx2, weight=0):
        if vtx1 not in self.vertexDic:
            self.addVertex(vtx1)
        if vtx2 not in self.vertexDic:
            self.addVertex(vtx2)
        self.vertexDic[vtx1].addNeighbor(self.vertexDic[vtx2], weight)

    def getVertices(self):
        return self.vertexDic.keys()

    def __iter__(self):
        return iter(self.vertexDic.values())


g = Graph()
for i in range(6):
    g.addVertex(i)

print(g.vertexDic)
print(g.getVertex(2))
