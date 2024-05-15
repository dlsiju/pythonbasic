from methodOverriding.Employee import Employee


class Doctor(Employee):

    def __init__(self, name, qualification, experience, noOfPatients, salary):
        super().__init__(name, qualification, experience, salary)
        self.noOfPatients = noOfPatients

    def totalSalary(self):
        return super().totalSalary() + self.noOfPatients * 150

    def displayNumberOfPatients(self):
        print('Number of Patients: ', self.noOfPatients)
