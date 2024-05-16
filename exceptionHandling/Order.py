from exceptionHandling.OutOfStock import OutOfStock
from exceptionHandling.Product import Product


class Order:
    product = None

    def __init__(self):
        self.product = Product(1, 'Book', 25)

    def placeOrder(self):
        print('shop name=', self.product._shopName, 'from', self.product._location)
        print('only', self.product._getStockAvailable(), ' are left')
        booksCount = int(input('Enter the number of books do you want to purchase:'))
        if booksCount > self.product._getStockAvailable():
            raise OutOfStock('Only {} books are available'.format(self.product._getStockAvailable()))
        print('order placed for {} books'.format(booksCount))


order = Order()
order.placeOrder()
