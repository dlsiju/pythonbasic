class Employee:

    def __init__(self, name, qualification, experience, salary):
        self.name = name
        self.qualification = qualification
        self.experience = experience
        self.salary = salary

    def totalSalary(self):
        return self.salary
