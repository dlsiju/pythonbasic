class Student:
    __passMark = 50
    __CollageName = 'University college'

    def __init__(self, rollnumber, name, totalMark):
        self.rollnumber = rollnumber
        self.name = name
        self.totalMark = totalMark

    @classmethod
    def getTotalMarks(cls, studnetlist):
        print('all students size=', studnetlist.__len__())
        return list(filter(lambda student: student.totalMark < cls.__passMark, studnetlist))

    @classmethod
    def displayAll(cls, failedStudentList):
        print('College name=', cls.__CollageName)
        print('failed students details are')
        for student in failedStudentList:
            print(student.rollnumber, student.name, student.totalMark)


student1 = Student(100, 'John', 35)
student2 = Student(200, 'Mary', 77)
student3 = Student(300, 'John', 40)
student4 = Student(400, 'Ram', 78)
student5 = Student(500, 'sita', 80)
student6 = Student(600, 'Sam', 57)
listofFailedStudents = Student.getTotalMarks([student1, student2, student3, student4, student5, student6])
print(type(listofFailedStudents))
print(listofFailedStudents.__len__())
Student.displayAll(listofFailedStudents)
