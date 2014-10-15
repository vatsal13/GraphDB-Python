__author__ = 'vatsal'

import Graph
import GraphDB
import MySQLdb

# all Query on the Graph Database ; querying the populated graph data-structure
class Query:

    g1=Graph.Graph()

    def __init__(self,g1):
        g=GraphDB.GraphDB()
        self.db=g.get_access()
        self.g1=g1


    # returns all in and out connected nodes
    def getNeighbour(self,key):

        v=self.g1.getVertex(key)
        if(v==None):
            print " -- No relations exists"
            return
        print v.id
        x=v.connectedToIn
        y=v.connectedToOut
        print ""
        for a,b in x.iteritems():
            print " --IN-- ",
            print "( ID = ", a.id,
            print "; Relation = ",b," ) ----",
            self.expandId(a.id)

        for a,b in y.iteritems():
            print " --OUT-- ",
            print "( ID = ", a.id,
            print "; Relation = ",b," ) ----",
            self.expandId(a.id)


    # Get the Details of a node with input as Key-Value
    def expandId(self,key):
        l1=key.split(':')
        cursor = self.db.cursor()
        try:
            sql=""" Select * from """+l1[0]+""" where ID= """+l1[1]
            #print sql
            cursor.execute(sql)
            results = cursor.fetchone()

            cursor = self.db.cursor()
            sql=""" SELECT column_name FROM information_schema.columns WHERE table_name = '"""+l1[0]+"""'"""
            cursor.execute(sql)
            results2 = cursor.fetchall()
            i=0
            print " | ",
            for r in results2:
                print r[0],":",results[i]," | ",
                i=i+1
            print ""

        except MySQLdb.Error,e:
            print "Error %d: %s" % (e.args[0],e.args[1])


    # Gives shortest path between 2 nodes with input of respective Key-Values
    def shortPath(self,k1,k2):
        path=self.find_shortest_path2( k1, k2,"start", path=[[] for i in range(2)] )

        for i in range(0, len(path[0])):
            print " -- ",path[1][i]," -- (",path[0][i],")",

    # does the computation after call from the above function
    def find_shortest_path2(self, start, end, rel, path=[[] for i in range(2)] ):
        path[0] = path[0] + [start]
        path[1] = path[1] + [rel]

        if (start == end):
            return path

        v=self.g1.getVertex(start)
        if(v==None):
            return None

        shortest = [[] for i in range(2)]
        for node in v.connectedToOut:
            if node.id not in path[0]:
                newpath = self.find_shortest_path2( node.id , end, v.connectedToOut[node],path)
                if newpath[0]:
                    if not shortest[0] or len(newpath[0]) < len(shortest[0]):
                        shortest[0] = newpath[0]
                        shortest[1] = newpath[1]
        return shortest


    # Gives all mutual connections between 2 nodes with Key-Value input
    def mutualConnect(self,k1,k2):
        v1=self.g1.getVertex(k1)
        v2=self.g1.getVertex(k2)
        i=0
        for x in v1.connectedToOut:
            for y in v2.connectedToOut:
                if(x==y):
                    i=1
                    print x.id
        if(i==0):
            print "None"