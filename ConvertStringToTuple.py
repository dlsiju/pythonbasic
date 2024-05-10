# .Convert a string to list of tuples.

input = "Python is the popular programming language."
print('input =', input)
listOfWords = input.split(" ")
listOfTuple = []
for i in range(0, len(listOfWords), 2):
    tuple2 = (listOfWords[i], listOfWords[i + 1])
    listOfTuple.append(tuple2)
print('list=', listOfTuple)
