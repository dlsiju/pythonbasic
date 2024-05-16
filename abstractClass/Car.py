from abstractClass.Driving import Driving


class Car(Driving):

    def drive(self):
        print("Driving the car")

    def nonAbstractMethod(self):
        print('Non-abstract method in car class invoked by', type(self).__name__)
