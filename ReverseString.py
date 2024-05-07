inputString = input("Enter a string: ")
print('input string:', inputString)
print('Reversed string using slice operator:', inputString[::-1])
reversedString = ''
for index in range(0, len(inputString)):
    reversedString = reversedString + inputString[-(index + 1)]
print('reversed string by iterating each character:', reversedString)
