from abc import ABC


class DbConnection(ABC):

    def connectToDb(self):
        pass

    def disconnect(self):
        pass
