import csv

csvFile = open('resource/day.csv', 'r')
reader = csv.reader(csvFile)
for row in reader:
    print(row)
print('number of line in csv file=', reader.line_num)
