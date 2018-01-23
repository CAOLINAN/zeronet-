# coding=utf-8
# @File  : PriceDB.py
# @Author: PuJi
# @Date  : 2018/1/22 0022
import sqlite3

class DB(object):
    def __init__(self, path):
        self.path = path
        print "Opened database successfully"
    def getCursor(self):
        self.conn = sqlite3.connect(self.path)
        return self.conn.cursor()

    def execute(self):
        c = self.getCursor()
        c.execute('''CREATE TABLE IF NOT EXISTS COMPANY
               (ID INT PRIMARY KEY     NOT NULL,
               NAME           TEXT    NOT NULL,
               AGE            INT     NOT NULL,
               ADDRESS        CHAR(50),
               SALARY         REAL);''')
        print "Table created successfully"
        self.conn.commit()
        self.conn.close()

    def insert(self):
        c = self.getCursor()
        c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )")

        c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

        c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

        c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

        self.conn.commit()
        print "Records created successfully"
        self.conn.close()

if __name__ == '__main__':
    d = DB('test.db')
    d.execute()
    d.insert()