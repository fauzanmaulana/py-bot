import mysql.connector

class Model:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connection(self):
        return mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)

    
    def selectAll(self, conn):
        cursor = conn.cursor()
        cursor.execute("SELECT nama, umur, ttl FROM students")
        result = cursor.fetchall()
        return result


model = Model('localhost', 'root', '', 'xirpl1')

conn = model.connection()

