# 1.Write a program to remove 10,20,30 from set1 = {10, 20, 30, 40, 50}

set1 = {10, 20, 30, 40, 50}
print('set1 =', set1)
set1.remove(10)
set1.remove(20)
set1.remove(30)
print('set1 after removal=', set1)
try:
    set1.remove(150)
except KeyError:
    print('Error while removing element')
