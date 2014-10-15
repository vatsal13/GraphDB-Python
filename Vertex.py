__author__ = 'vatsal'

class Vertex:

    # Key is string which combines sql table name and the row id eg. 'Student:2' ; Student->Table Name ; 2->RowId
    # connectedToOut: Dict that stores all out-edges and nodes connected to
    # connectedToIn: Dict that stores all in-edges and nodes connected to
    def __init__(self,key):
        self.id = key
        self.connectedToOut = {}
        self.connectedToIn = {}

    def addNeighborOut(self,nbr,rel):
        self.connectedToOut[nbr] = rel

    def addNeighborIn(self,nbr,rel):
        self.connectedToIn[nbr] = rel

    def getConnections(self):
        return self.connectedToOut.keys()

    def getId(self):
        return self.id

    def getRelation(self,nbr):
        return self.connectedToOut[nbr]