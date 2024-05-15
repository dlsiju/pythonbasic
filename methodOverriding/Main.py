from methodOverriding.Doctor import Doctor
from methodOverriding.NursingStaff import NursingStaff

doctor1 = Doctor('Hari', 'MS', 4, 10, 50000)

print('Doctor details are')
doctor1.displayEmployeeDetails()
doctor1.displayNumberOfPatients()
doctorSalary = doctor1.totalSalary()
print('doctor total salary is', doctorSalary)

nurse1 = NursingStaff('Liza', 'B.Sc', 5, 20000, 20)
print('\nNurse details are')
nurse1.displayEmployeeDetails()
nurse1.displayNumberOfExtraHours()
nurseSalary = nurse1.totalSalary()
print('nurse total salary is', nurseSalary)
