import os
import random

# get random value from list
colorList = ['red', 'blue', 'green', 'yellow', 'black', 'white']
randomColor = random.choice(colorList)
print('The random color is: ' + randomColor)

numberSet = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(random.choices(list(numberSet)))

# get random value from set
car_details = {
    "Vehicle": "Car",
    "Fuel": 'Petrol',
    "Price": '300000',
    "model": "i10"
}
randomValueFromDictionary = random.choice(list(car_details.values()))
print('randomValueFromDictionary is: ' + randomValueFromDictionary)

# Get random filename from directory and read text file

fileList = os.listdir('C:/Users/XM-Laptop17/Siju test')
st = random.choice(fileList)
print('FileName=', st)
fil = open('C:/Users/XM-Laptop17/Siju test/' + st, 'r')
for line in fil:
    print(line)
