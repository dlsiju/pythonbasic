from methodOverriding.Employee import Employee


class Doctor(Employee):

    def __init__(self, name, qualification, experience, noOfPatients, salary):
        super().__init__(name,qualification,experience,salary)
        self.noOfPatients = noOfPatients

    def totalSalary(self):
        print('super().totalSalary()=', super().totalSalary())
        print('self.noOfPatients*150=', self.noOfPatients * 150)
        return super().totalSalary() + self.noOfPatients * 150
