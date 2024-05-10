# 1.Write a program to modify first item of list in the following tuple

tuple1 = (11, [22, 33], 44, 55)
print('tuple1=', tuple1)
convertedList = list(tuple1)
print('convertedList=', convertedList)
convertedList[0] = 12
print('convertedList after updated first item=', convertedList)
updatedTuple = tuple(convertedList)
print(u'tuple1=', updatedTuple)
