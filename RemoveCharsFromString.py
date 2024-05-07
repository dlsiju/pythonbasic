inputString = input('Enter a string: ')

filterString = "".join(c for c in inputString if c.isnumeric())
print('filtered string using .join()=', filterString)

for char in inputString:
    if not char.isnumeric():
        inputString = inputString.replace(char, '')
print('filtered string using for each loop=', inputString)