from abstractClass.DbConnection.MySQL import MySQL
from abstractClass.DbConnection.Postgres import Postgres


class MainConnection:
    mysql = MySQL()
    mysql.connectToDb()
    postgres = Postgres()
    postgres.connectToDb()
    postgres.disconnect()
    mysql.disconnect()
