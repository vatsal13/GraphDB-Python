__author__ = 'vatsal'

import MySQLdb
import GraphDB
import Graph

# Define and create new edges
class Relation:

    g1=Graph.Graph()

    def __init__(self,g1):
        g=GraphDB.GraphDB()
        self.db=g.get_access()
        self.g1=g1

    # Define the type of edge before adding that edge , if not previously defined.
    def defRel(self,type):
        cursor = self.db.cursor()
        try:
            sql=""" CREATE TABLE `"""+type+"""`(`Type1` varchar(255),`id1` int,`Type2` varchar(255),`id2` int ,PRIMARY KEY ( Type1, id1, Type2, id2))"""
            cursor.execute(sql)
            i=1
        except MySQLdb.Error,e:
            print "Error %d: %s" % (e.args[0],e.args[1])
            i=2
        if(i==1):
            sql="""INSERT INTO RELATION (name) VALUES ('"""+type+"""')"""
            cursor.execute(sql)
            self.db.commit()


    # Add an edge between 2 node with providing : the edge type, and Key-Value of the 2 nodes
    def newRel(self,type,key1,key2):
        l1=key1.split(':')
        l2=key2.split(':')
        cursor = self.db.cursor()
        try:
            sql=""" INSERT INTO `"""+type+"""` (Type1,id1,Type2,id2) VALUES ('"""+l1[0]+"""',"""+l1[1]+""",'"""+l2[0]+"""',"""+l2[1]+""")"""
            cursor.execute(sql)
            self.db.commit()
            self.g1.addEdge(key1,key2,type)
        except MySQLdb.Error,e:
            print "Error %d: %s" % (e.args[0],e.args[1])



