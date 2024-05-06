def IsDivisibleByFiveOrSeven(num):
    if num % 5 == 0 and num % 7 == 0:
        print('number', num, 'is divisible both by 5 or 7')
    else:
        print('number', num, 'is not divisible by both  5 or 7')


try:
    numberToCheck = int(input('Enter a number: '))
    IsDivisibleByFiveOrSeven(numberToCheck)
except ValueError:
    print('Please enter a valid integer')
