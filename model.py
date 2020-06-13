import mysql.connector

class Model:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.cursor = ""

    def connection(self):
        return mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)

    
    def selectAll(self, conn):
        self.cursor = conn
        print(self.cursor)


model = Model('localhost', 'root', '', 'xirpl1')

conn = model.connection().cursor()

