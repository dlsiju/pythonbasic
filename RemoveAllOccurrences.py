# 3.Remove all occurrences of a specific item from a list.

colorList = ['red', 'green', 'blue', 'red', 'green', 'indigo', 'yellow', 'red', 'violet', 'white', 'black', 'orange']
print('list1 =', colorList)
itemTobeRemoved = input('enter any item to remove if it is present')
print('item to remove =', itemTobeRemoved)
colorList = [item for item in colorList if item != itemTobeRemoved]
print('list1 after removal =', colorList)
