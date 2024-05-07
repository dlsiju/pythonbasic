def keyWordArgsConcatenation(**keykwds):
    appendedstring = ''
    for key in keykwds.keys():
        appendedstring += keykwds[key]
    return appendedstring


print('Enter four string values to concatenate using keyword arguments:')
firstString = input('First string: ')
secondString = input('Second string: ')
thirdString = input('Third string: ')
fourthString = input('Fourth string: ')
appendedStringValue = keyWordArgsConcatenation(third=thirdString, second=secondString, fourth=fourthString,
                                               first=firstString)
print("Appended String:", appendedStringValue)
