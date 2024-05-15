from methodOverriding.Doctor import Doctor
from methodOverriding.NursingStaff import NursingStaff

doctor1 = Doctor('Hari', 'MS', 4, 10, 50000)

doctorSalary = doctor1.totalSalary()
print('doctor salary is', doctorSalary)

nurse1 = NursingStaff('Liza', 'B.Sc', 5, 20, 20000)

nurseSalary = nurse1.totalSalary()
print('nurse salary is', nurseSalary)