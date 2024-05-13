import copy

numberList = [1, 2, 3, 4, 5, [60, 70], 6, 7, 8, 9]
print('numberList=', numberList)
listShallowCopy = copy.copy(numberList)
print('listShallowCopy=', listShallowCopy)
listShallowCopy[5][1] = 10
print('shallow copy after updating the inner list=', listShallowCopy)
print('original list after updating the inner list of shallow copy=', numberList)
