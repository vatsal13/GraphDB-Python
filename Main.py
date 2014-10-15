__author__ = 'vatsal'

import GraphDB
import MySQLdb

# Main python file : Populates the Graph with the SQL database
g=GraphDB.GraphDB()
db=g.get_access()

# Populates the Graph Data-Structure from the SQL
# Goes through all existing Tables creating the nodes and edges : Graph DB
def populate(g1):
    cursor = db.cursor()
    try:
        sql="""CREATE TABLE RELATION (name varchar(255),PRIMARY KEY (name))"""
        cursor.execute(sql)

    except MySQLdb.Error,e:
            print "LOG -> %d: %s" % (e.args[0],e.args[1])

    try:
            # RELATION stores all types of edges
            sql="""select * from RELATION"""
            cursor.execute(sql)
            res=cursor.fetchall()

            for r in res:
                sql="""select * from """+r[0]
                cursor.execute(sql)
                res2=cursor.fetchall()
                for x in res2:
                    type1=x[0]
                    id1=x[1]
                    type2=x[2]
                    id2=x[3]
                    id1=type1+":"+str(id1)
                    id2=type2+":"+str(id2)
                    g1.addEdge(id1,id2,r[0])

    except MySQLdb.Error,e:
            print "Error %d: %s" % (e.args[0],e.args[1])


# Returns the Key-Value of a Node with query parameters which should include all /
# unique parameters atleast.
def getKey(type,**kwargs):
    # where clause for sql statement
    where=""
    i=0
    for k,v in kwargs.iteritems():
        i=i+1
        where=where+" "+k+"="+"'"+v+"'"
        if(i<len(kwargs)):
            where=where+" and "

    cursor = db.cursor()
    sql="""SELECT ID FROM """+type+""" WHERE """+where
    cursor.execute(sql)
    results = cursor.fetchall()
    if(cursor.rowcount==1):
        for a in results:
            s= a[0]
        return type+":"+str(s)
    else:
        print "No UNIQUE key"
        # returns NULL if parameters do not contain all unique values
        return "NULL"



