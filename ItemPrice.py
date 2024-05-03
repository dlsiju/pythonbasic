itemList = [['book', 30], ['pen', 20], ['pencil', 5], ['bag', 320], ['watch', 560], ['ring', 1500]]

item = input('Enter the item which you want to know the price:')
match item:
    case 'book':
        print('price:', itemList[0][1])
    case 'pen':
        print('price:', itemList[1][1])
    case 'pencil':
        print('price:', itemList[2][1])
    case 'bag':
        print('price:', itemList[3][1])
    case 'watch':
        print('price:', itemList[4][1])
    case 'ring':
        print('price:', itemList[5][1])
    case _:
        print('item not available')
