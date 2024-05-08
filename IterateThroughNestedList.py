# 5.Iterate through the following nested list using for loop and print the elements


nestedList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('values in the nested list using single for loop are follows,')
for list in nestedList:
    print(*list, end=" ")

print('\nvalues in the nested list using nested for loop are follows,')
for list in nestedList:
    for element in list:
        print(element, end=" ")
