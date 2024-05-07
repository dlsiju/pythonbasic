inputString = input("Enter a string: ")
searchKey = input('Enter a search key')
index = 0
indexList = []
occurrenceCount = 0
inputString = inputString.casefold()
while index < len(inputString):
    if inputString.startswith(searchKey.casefold(), index):
        occurrenceCount += 1
        indexList.append(index)
    index += 1
print(searchKey, 'found on indexes', indexList)
print(searchKey, ' has been found ', occurrenceCount, ' time in the given string')
