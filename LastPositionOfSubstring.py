inputString = input("Enter a string: ")
searchKey = input('Enter the string to find its last position: ')
inputString = inputString.casefold()
indexFound = 0
check = lambda x: x if inputString.startswith(searchKey.casefold(), x) else indexFound

for i in range(len(inputString)):
    indexFound = check(i)
print('last occurance of string', searchKey, ' is', indexFound)
