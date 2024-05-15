class Employee:

    def __init__(self, name, qualification, experience, salary):
        self.name = name
        self.qualification = qualification
        self.experience = experience
        self.salary = salary

    def totalSalary(self):
        return self.salary

    def displayEmployeeDetails(self):
        print('name=', self.name)
        print('qualification=', self.qualification)
        print('experience=', self.experience)
        print('Fixed salary=', self.salary)
