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
        cursor.execute("SELECT nama FROM students")
        result = cursor.fetchall()
        return result

    def searchData(self, conn, name):
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM students where nama LIKE " + "'" + name + "'")
        result = cursor.fetchone()
        return result

    def showData(self, conn, id):
        cursor = conn.cursor()
        cursor.execute("SELECT nama, umur, ttl, alamat FROM students where id = " + id)
        result = cursor.fetchone()
        return result


model = Model('localhost', 'root', '', 'xirpl1')

conn = model.connection()

