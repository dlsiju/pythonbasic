class Product:
    __id = None
    __name = None
    __stockAvailable = None
    _location = "Trivandrum"
    _shopName = 'Green Shop'

    def __init__(self, id, name, stockAvailable):
        self.__id = id
        self.__name = name
        self.__stockAvailable = stockAvailable

    def _getProductId(self):
        return self.__id

    def _get__name(self):
        return self.__id

    def _getStockAvailable(self):
        return self.__stockAvailable
