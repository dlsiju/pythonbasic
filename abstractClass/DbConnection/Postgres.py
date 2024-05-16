from abstractClass.DbConnection.Dbconnection import DbConnection


class Postgres(DbConnection):

    def connectToDb(self):
        print('connecting to Postgres database...')

    def disconnect(self):
        print('disconnecting from Postgres database...')
