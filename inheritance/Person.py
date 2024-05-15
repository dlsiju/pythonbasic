class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def displayData(self):
        print('Name:', self.name)
        print('Age:', self.age)
        print('Height:', self.height)
        print('Weight:', self.weight)
