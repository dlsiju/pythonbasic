import random
import string

# Generating random number between specific range

num1 = 30
num2 = 50
randomNumber = random.randint(num1, num2)
print('random number is', randomNumber)

length = int(input('Press Enter the length for random string'))
# Generate random alphabetical String
randomString = ''.join(random.choice(string.ascii_uppercase) for i in range(27))
print('random string is', randomString)

# Generate random string using while loop
randomStringByLoop = ''
while 1:
    randomNumber = random.randint(0, 25)
    randomStringByLoop += string.ascii_uppercase[randomNumber]
    if len(randomStringByLoop) >= length:
        break;
print('randomStringByLoop=', randomStringByLoop)

# Generate random color hex

randomForHex = random.randint(0, 2 ** 24)
print('random number is', randomForHex)
hexString = hex(randomForHex)
print('hexString=', hexString)

# Generate random mulitple of 7 between o and 70
nubmerSet = set()
while 1:
    randomNumber = random.randint(0, 69)
    if randomNumber % 7 == 0:
        nubmerSet.add(randomNumber)
        if len(nubmerSet) > 9:
            break;
print('random number divisibl by 7=', nubmerSet)
