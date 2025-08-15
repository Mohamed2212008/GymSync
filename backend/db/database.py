import sqlite3

class Database:
    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name)
        self.con("PRAGMA foreign_keys = ON")
        self.cur = self.con.cursor()

    def execute(self, query, param = None):
        if param == None:
            self.cur.execute(query)
            self.con.commit()
        else:
            self.cur.execute(query, param)
            self.con.commit()

    def fetchall(self, table):
        self.cur.execute(f'SELECT * FROM {table}')
        data = self.cur.fetchall()
        return data

    def fetchone(self, table):
        self.cur.execute(f"SELECT * FROM {table}")
        data = self.cur.fetchone()
        return data
    
    def remove(self,table, statement, value):
        self.cur.execute(f'DELETE FROM {table} WHERE {statement} = {value}')
        self.con.commit()

    def close_con(self):
        self.con.close()