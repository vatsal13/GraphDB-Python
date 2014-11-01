GraphDB-Python
==============

Documentation - Graph Database over SQL
A graph database over SQL using Python

_____________________________________________________________________________________

A.	Graph representation:

1.	2D matrix:
Space complexity = O(V2)
Complexity to identify all neighbors = O(V)

2.	Edge list:
Space complexity =O(E)
But proves useful only for certain operations.

3.	Adjacency List:
Space complexity=O(V+E).
max(E)=(V*(V-1))/2  but usually E <  max(E) for most of the cases.

Therefore space complexity < O(V2) most of the time.
For k neighbors the time complexity to travers all of them id O(k) < O(V)

Thus adjacency List is used to represent the graph data-structure.

_____________________________________________________________________________________

B.	Approach:

1.	RELATIONS Table: 
It stores the names of all types of edges in the Graph.

Name
Manages
Teaches
friends_with

2.	Table for each type of node:
 Every type of node has a table with the table name as  the type. All nodes of the same type are in the same table.

ID	Name	Age	School
1	Vatsal	21	SCSE
2	Hiten	22	SCSE
Eg: Student Table

ID column is auto increment , and exists for all tables. The no. of columns may vary depending on the user.

3.	Table for each type of edge:
 Every type of edge also has a table with table name as that of the type. All edges of same type are in the same table.

Type1	Id1	Type2	Id2
Student	1	Student	3
Teacher	2	Teacher	7
Manager	2	Student	4
Eg: ‘knows’ relation table

(Type1,id1,Type2,id2) all 4 fields form the edge/relation table and all together from the unique key too. Thus each row represents one edge between 2 nodes. Type specifies the node’s table name and id specifies the row id in that table. It shows a directed edge from right type node to left type node.

Student:1  Student:3


4.	Key-Value for each node:
Key-Value= “TableName”+”:”+”RowId”

ID	Name	Age	School
1	Vatsal	21	SCSE
2	Hiten	22	SCSE
Eg: Student Table

Say if a new node with Name =”Hiten ” was created then ,a key would be returned with Key-Value = Student:2 . Thus each node created will always have an unique key containing information of its SQL table and row id.


5.	Populating the Graph data structure using SQL:
Go to RELATION table , and one by read the name of relation and go to the respective relation/edge table.
For each edge in edge table we create the 2 nodes in the graph if they do not already exist and add the edge and neighbor information in the adjacency list of each node.
Thus we only traverse the edge tables to create the graph.
The node tables are only accessed when more information about the node is needed except the Key-Value.


_____________________________________________________________________________________

C.	How to use:

1.	Initial Setup:
Run the code in a command line or IDLE. Write the commands:

>>> import sys
>>> sys.path.extend(['C:\\Users\\s\\proj2'])

Use the path where project is stored.

_____________________________________________________________________________________

2.	Import all files:

>>> import Graph,Vertex,Node,Query,GraphDB,Main,Relation

The Main file would make connection to the SQL database.

_____________________________________________________________________________________

3.	Create and initialize the graph db:

>>> g1=Graph.Graph()

Create an instance of Graph. 

>>> Main.populate(g1)

Use Main to call populate function by passing the Graph object. Now we can work on the graph database.

_____________________________________________________________________________________


4. Adding a Node:
*For now all node attribute all considered as string datatype. Thus create only string attributes.

>>> n=Node.Node()

>>> n.defNode("Student","`Name` U","`Age`","`School` U")

>>> n.newNode("Student","Vatsal","21","SCSE")
>>> n.newNode("Student","Abhishek","20","SCSE")

>>> n.defNode("Teacher","`Name` U","`Exp` U","`School`")

>>> n.newNode("Teacher","Rahul","5","MECH")
>>> n.newNode("Teacher","Wyan","10","SCSE")
>>> n.newNode("Student","Jalaj","20","SCSE")
>>> n.newNode("Teacher","Arun K","6","SCSE")

_______________________

>>>n=Node.Node()
Firstly create an object of class Node.

________________________
n.defNode("Student","`Name` U","`Age`","`School` U")

defNode: this function is used to define a new type of node. 
	
def defNode(self,type,*args):
	
type: type takes as input the type of node (/ name of node table)
	
*args: takes the input of  property names (column names in table) of the node. Mention the fields in “ ” . To enter column names /property name use ` ` followed by space and U (eg. "`Name` U" ). U is used to specify unique parameter. Each definition must have at least 1 unique parameter. There is no limit to property name (/ column names).

________________________

n.newNode("Student","Jalaj","20","SCSE")

newNode: this function is used to create a new node if its type is already defined.
	
def newNode(self,type,*args):
	
type: type takes as input  the type of node.
	
*args: takes input of various property values for the property attributes defined in defNode.  Enter the values in “ ”. 

_____________________________________________________________________________________
	
4.	Get the Key-Value:

>>> k1=Main.getKey("Student",Name="Vatsal",School="SCSE")

getKey: It returns the Key-Value for a node. 
	
def getKey(type,**kwargs):
	
type: Enter the type of node , to get the key for.
	**kwargs: here the input is the unique parameters of the node .There can be more parameters        but all unique parameters should be present. The input is a DIct thus use the property name/column name a Key and property value as value (eg. School="SCSE").

It would return NULL if unique values are missing.
*IF Null Key is entered into some function it would give error / crash.

_____________________________________________________________________________________

6.	Adding an Edge:

>>> r=Relation.Relation(g1)
>>> r.defRel("teaches")
>>> k1=getKey("Student",Name="Vatsal",School="SCSE")
>>> k2=getKey("Teacher",Name="Wyan",Exp="10")
r.newRel("teaches",k2,k1)

__________________

r=Relation.Relation(g1)

Firstly, create an object of class Relation and pass a Graph object.

__________________

r.defRel("teaches")

defRel: this function is used to define a new type of edge , such that the type does not previously exist

	def defRel(self,type):
	type: type takes input of the edge type one wants to create.

__________________

k1=getKey("Student",Name="Vatsal",School="SCSE")
k2=getKey("Teacher",Name="Wyan",Exp="10")

Get the keys of the nodes between edge is to established.

____________________

r.newRel("teaches",k2,k1)

newRel: this function is used to add an edge to the graph such that type has been previously defined.

	def newRel(self,type,key1,key2):
	type: type here is the type of edge
	key1 and key2: are the Key-Values of the desired nodes.


_____________________________________________________________________________________

D.	Querying the Graph DB:

>>> q=Query.Query(g1)

Firstly create an object of Query class to query the Graph DB. Pass a graph object to it.
_____________________________________________________________________________________

1.	Get all neighbors:

>>> k1=Main.getKey("Teacher",Name="Wyan",Exp="10")
>>> q.getNeighbour(k1)

Teacher:2

 --IN--  ( ID =  Manager:1 ; Relation =  manages  ) ----  |  ID : 1  |  Name : Jack  |  Age : 21  |  Company : TATA  |  
 --OUT--  ( ID =  Student:1 ; Relation =  teaches  ) ----  |  ID : 1  |  Name : Vatsal  |  Age : 21  |  School : SCSE  |  
 --OUT--  ( ID =  Student:4 ; Relation =  teaches  ) ----  |  ID : 4  |  Name : PIYUSH  |  Age : 20  |  School : MECH  |  

getNeighbour: this function takes input of the Key-Value of the node and returns the in-edge and out-edge neighbors, all with their details.
	
def getNeighbour(self,key):
	key: use the getKey( ) function to get key of a particular node . (eg. Manager:342)

It outputs the id of the neighbors and their edge relation too.

_____________________________________________________________________________________

2.	Get all details of a node:

>>> k1=Main.getKey("Teacher",Name="Wyan",Exp="10")
>>> q.expandId(k1)
 |  ID : 2  |  Name : Wyan  |  Exp : 10  |  School : SCSE  |   

expandId: this function takes the key as input and then refers the SQL database to retrieve all information for the particular key.
	def expandId(self,key):
	key: Key-Value , use getKey()

_____________________________________________________________________________________

3.	Get the shortest path between 2 nodes:

>>> k1=Main.getKey("Manager",Name="Suzen",Company="Parle")
>>> k2=Main.getKey("Student",Name="Vatsal",School="SCSE")
>>> q.shortPath(k1,k2)

 --  start  -- ( Manager:5 )  --  manages  -- ( Manager:1 )  --  manages  -- ( Teacher:2 )  --  teaches  -- ( Student:1 )

shortPath: this function takes input of the keys of 2 nodes and returns the shortest path between those 2 nodes.
	def shortPath(self,k1,k2):
	k1 and k2: these are the Key-Values for respective nodes

It returns nothing if there is no path between the 2 nodes.

_____________________________________________________________________________________

4.	Getting mutual connections between 2 nodes:

>>> k1=Main.getKey("Teacher",Name="Rahul",Exp="5")
>>> k2=Main.getKey("Teacher",Name="Wyan",Exp="10")
>>> q.mutualConnect(k1,k2)

Student:1

mutualConnect: this function returns common out-edge connections between 2 nodes.

	def mutualConnect(self,k1,k2):
	k1 and k2: these are the Key-Values for respective nodes.

It returns None if there is no mutual connection between the 2 nodes.

_____________________________________________________________________________________


