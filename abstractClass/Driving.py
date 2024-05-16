from abc import abstractmethod, ABC


class Driving(ABC):

    @abstractmethod
    def drive(self):
        pass

    def nonAbstractMethod(self):
        print('this is a non-abstract method in Driving class invoked by', type(self).__name__)
