__author__ = 'vatsal'

import MySQLdb
import GraphDB

# Define and Create new Nodes
class Node:

    def __init__(self):
        g=GraphDB.GraphDB()
        self.db=g.get_access()

    # Define the type of Node before adding that Node , if not previously defined.
    def defNode(self,type,*args):
        i=0
        query=""
        primKey=""
        i2=0
        for a in args:
            i=i+1
            l=a.split('`')
            if(len(l)==3):
                if(l[2]==" U"):
                    if(i2==1):
                        primKey=primKey+","
                    primKey=primKey+l[1]
                    i2=1
            query=query+"`"+l[1]+"`"+" "+"varchar(255)"
            query=query+","

        cursor = self.db.cursor()
        try:
            sql="""CREATE TABLE `"""+ type +"""` ( ID int NOT NULL AUTO_INCREMENT, """+ query +"""PRIMARY KEY (ID),UNIQUE ("""+primKey+""") )"""
            cursor.execute(sql)
        except MySQLdb.Error,e:
            print "Error: %s" % (e.args[1])


    # Add new node by providing they type of node and specifying various parameters/properties
    def newNode(self,type,*args):
        i=0
        query=""
        for a in args:
            i=i+1
            p=1
            if (i==len(args)):
                p=0
            query=query+"'"+a+"'"
            if(p==1):
                query=query+","

        cursor = self.db.cursor()
        sql=""" SELECT column_name FROM information_schema.columns WHERE table_name = '"""+type+"""'"""
        cursor.execute(sql)
        results = cursor.fetchall()
        temp=""
        i=0
        for row in results:
                i=i+1
                if(i==1):
                    continue
                temp=temp+row[0]
                if(i<len(results)):
                    temp=temp+","
        try:
            cursor = self.db.cursor()
            sql="""INSERT INTO `"""+ type +"""` ("""+temp+""") VALUES ("""+ query +""")"""
            cursor.execute(sql)
            self.db.commit()
        except MySQLdb.Error,e:
            print "Error %d: %s" % (e.args[0],e.args[1])




