# 4.Insert item ‘dd’ to the second sublist’s first position


list = ['a', ['bb', 'cc'], 'd']
print('initial values in list=', list)
list[1].insert(0, 'dd')
print('list after inserted dd as first element in second sublist=', list)
