from inheritance.Person import Person


class Student(Person):

    def __init__(self, name, age, height, weight):
        super().__init__(name, age, height, weight)


student1 = Student('John', 26, 180, 80)
print('Details of student1 are:')
student1.displayData()
student2 = Student('Ram', 30, 160, 50)
print('Details of student2 are:')
print('Name:', student2.name)
print('Age:', student2.age)
print('Height:', student2.height)
print('Weight:', student2.weight)
