from connection import mysql

class getDatas(object):
    def __init__(self):
        self.cursor=mysql.connect().cursor()

    def getAlldata(self):
        self.cursor.execute("SELECT * FROM user")
        adata=self.cursor.fetchall()
        return adata
