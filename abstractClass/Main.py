from abstractClass.Bus import Bus
from abstractClass.Car import Car
from abstractClass.Driving import Driving


class Main:
    bus = Bus()
    bus.drive()
    bus.nonAbstractMethod()
    car = Car()
    car.drive()
    car.nonAbstractMethod()
    try:
        driving = Driving()
    except TypeError:
        print('instantiation failed for class driving')
