listSize = int(input("Enter size of list: "))
listOfKeyword = []
for i in range(0, listSize):
    listOfKeyword.append(input('Enter keyword: '))
print('list of keyword=', listOfKeyword)
while '' in listOfKeyword:
    listOfKeyword.remove('')
print('list of keywords after removal of empty space=', listOfKeyword)
