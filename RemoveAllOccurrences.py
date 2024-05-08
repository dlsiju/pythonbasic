# 3.Remove all occurrences of a specific item from a list.

list1 = ['red', 'green', 'blue', 'red', 'green', 'indigo', 'yellow', 'red', 'violet', 'white', 'black', 'orange']
print('list1 =', list1)
itemTobeRemoved = input('enter any item to remove if it is present')
print('item to remove =', itemTobeRemoved)
list1 = [item for item in list1 if item != itemTobeRemoved]
print('list1 after removal =', list1)
