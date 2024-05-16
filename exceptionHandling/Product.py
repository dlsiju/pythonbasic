class Product:
    id = None
    name =None
    stockAvailable = None

    def __init__(self, id, name, stockAvailable):
        self.__id = id
        self.name = name
        self.stockAvailable = stockAvailable
