inputString = input("Enter a string: ")
print('inputString=', inputString)
searchKey = input('Enter a search key')
print('searchKey=', searchKey)
index = 0
indexList = []
occurrenceCount = 0
while index < len(inputString):
    if inputString.startswith(searchKey, index):
        occurrenceCount += 1
        indexList.append(index)
    index += 1
print(searchKey, 'found on indexes', indexList)
print(searchKey, ' has been found ', occurrenceCount, ' time in the given string')
