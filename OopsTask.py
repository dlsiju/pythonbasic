import datetime


class Book:

    def __init__(self, id, name, author, year,month,date):
        self.id = id
        self.name = name
        self.author = author
        self.publish_date = datetime.datetime(year,month,date)

    def print_book(self):
        print('name of book:', self.name)

    def change_book_name(self):
        self.name=input('enter new name for book:')


book = Book(1, 'crazy', 'Tom', 2024,3,21)
book.print_book()
needToChange = input('Do you want to change the name? (y/n) ')
if needToChange =='y':
    book.change_book_name()
    print("After updating book name")
    book.print_book()
print('book has an attribute named author? ',hasattr(book, 'author'))
print('publish_date of book: ',book.publish_date)
del book.publish_date
print('book has an attribute named publish_date? ',hasattr(book, 'publish_date'))
