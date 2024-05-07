import string

inputString = input("Enter a string: ")
print('Original string=', inputString)
reformatString = "".join(filter(lambda x: x not in string.punctuation, inputString))
print('reformatted string:', reformatString)
