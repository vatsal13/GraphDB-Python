__author__ = 'vatsal'

import MySQLdb

# Connect to database hosted on www.freemysqlhosting.net
class GraphDB:

    def __init__(self):
        self.db1 = MySQLdb.connect("sql3.freemysqlhosting.net","sql354178","wR2!kY7%","sql354178" )

    def close(self):
        self.db1.close()

    # returns an instance of database
    def get_access(self):
        return self.db1