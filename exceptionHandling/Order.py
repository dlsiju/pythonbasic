from exceptionHandling.OutOfStock import OutOfStock
from exceptionHandling.Product import Product


class Order:
    product = None

    def __init__(self):
        self.product = Product(1, 'Book', 25)
        print(self.product.id)
        print(self.product.name)
        print(self.product.stockAvailable)

    def placeOrder(self):
        booksCount = int(input('Enter the number of books do you want to purchase:'))
        if booksCount > self.product.stockAvailable:
            raise OutOfStock('Only {} books are available'.format(self.product.stockAvailable))
        print('order placed for {} books'.format(booksCount))


order = Order()
order.placeOrder()
