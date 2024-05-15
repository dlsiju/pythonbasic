from methodOverriding.Employee import Employee


class NursingStaff(Employee):

    def __init__(self, name, qualification, experience, salary, noOfExtraHours):
        super().__init__(name, qualification, experience, salary)
        self.noOfExtraHours = noOfExtraHours

    def totalSalary(self):
        return super().totalSalary() + self.noOfExtraHours * 100

    def displayNumberOfExtraHours(self):
        print('Number of extra hours: ', self.noOfExtraHours)
