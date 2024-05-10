
#2.Write a program to return a set of elements present in set1 or set2, but not both


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print('set1 =', set1)
print('set2 =', set2)
intersectionSet = set1.intersection(set2)
diff=set1.union(set2)-set1.intersection(set2)
print('set of elements from both list but not common elements=',diff)
print('Common elements from both list =',intersectionSet)


