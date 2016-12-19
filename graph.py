class Vertex:
    __slots__ = ['id', 'connectedTo', 'bfsDepth', 'previous']
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.bfsDepth = 0
        self.previous = None

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connectedTo])

class Graph:
    __slots__ = ['vertices', 'numVertices', 'numEdges']
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0
        self.numEdges = 0

    def addVertex(self, key):
        if self.vertices.get(key):
            raise 'vertex already exists'
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def addEdge(self, fromVert, toVert, weight=0, directed=True):
        if toVert == fromVert: raise "Can't Connect Vertex to Self"
        f = self.getVertex(fromVert) or self.addVertex(fromVert)
        t = self.getVertex(toVert) or self.addVertex(toVert)
        f.addNeighbor(t, weight)
        self.numEdges += 1
        if not directed:
            t.addNeighbor(f, weight)

    def getVertex(self, vertKey):
        return self.vertices.get(vertKey)

    def getVertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

    def __str__(self):
        for v in self.vertices.values():
            print(v)
        return ''

    def __contains__(self, n):
        return n in self.vertices
