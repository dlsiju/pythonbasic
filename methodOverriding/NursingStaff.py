from methodOverriding.Employee import Employee


class NursingStaff(Employee):

    def __init__(self, name, qualification, experience, noOfPatients, salary):
        super().__init__(name,qualification,experience,salary)
        self.noOfPatients = noOfPatients

    def totalSalary(self):
        print('super().totalSalary()=', super().totalSalary())
        print('self.noOfPatients*100=', self.noOfPatients * 100)
        return super().totalSalary() + self.noOfPatients * 100
