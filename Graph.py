__author__ = 'vatsal'

# Graph Data-structure using Adjacency List
# Directed Graph
import Vertex

class Graph:

    # maintains a list of all vertices : vertList
    # maintains count of vertices : numvertices
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    # each node is accessed using unique Key Value
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex.Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    # f : vertex1
    # t : vertex2
    # rel : edge-type
    def addEdge(self,f,t,rel):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        # adding out-edges
        self.vertList[f].addNeighborOut(self.vertList[t], rel)
        # keeping track of in-edges
        self.vertList[t].addNeighborIn(self.vertList[f], rel)

    # returns vertex instance from key
    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())