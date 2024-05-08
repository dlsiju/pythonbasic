
#1.Iterate both lists simultaneously use zip method.

list1 = [10, 20, 30, 40]
list2 = [50, 60, 70, 80]
zippedList = zip(list1, list2)

for zItem in zippedList:
    print('lis1={}, lis2={}'.format(zItem[0], zItem[1]))

items = ['apple', 'orange', 'mango', 'chocolate', 'cake', ]
quantityInKg = [2, 3, 2.5, 1, 1]
price = [345, 450, 100, 400, 250]

zipped = zip(items, quantityInKg, price)
for zippedItem in zipped:
    print(zippedItem[2], ' rupees for ', zippedItem[1], ' KG of ', zippedItem[0])
