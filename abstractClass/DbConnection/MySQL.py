from abstractClass.DbConnection.Dbconnection import DbConnection


class MySQL(DbConnection):

    def connectToDb(self):
        print('connecting to MySQL database...')

    def disconnect(self):
        print('disconnecting from MySQL database...')
