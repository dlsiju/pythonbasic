def average(numbers):
    total = 0
    avg = 0;
    for n in numbers:
        total += n;
    avg = total / len(numbers)
    return avg


try:
    inputCount = int(input('enter total number of elements'))
    list = [0] * inputCount
    index = 0;
    while index < inputCount:
        list[index] = int(input('enter each number'));
        index += 1
    averageOfNumber = average(list)
    print('average of all number =', averageOfNumber)
except:
    print("Please enter a valid number")
