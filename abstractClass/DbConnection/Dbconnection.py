from abc import abstractmethod, ABC


class DbConnection(ABC):

    @abstractmethod
    def connectToDb(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass
