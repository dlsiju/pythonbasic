def show_employee(id, name, title, dept, sal=9000):
    print("THE employee details are follows")
    print('ID=', id)
    print('NAME=', name)
    print("TITLE=", title)
    print("DEPARTMENT=", dept)
    print("SALARY=", sal)


try:
    id = int(input('Enter the id'))
    name = input('Enter the name')
    job_title = input('Enter the job title')
    department = input('Enter the department')
    salary = int(input('Enter the salary, or enter zero if no custom salary specified'))
    show_employee(id, name, job_title, department, salary) if salary != 0 else show_employee(id, name, job_title,
                                                                                             department)
except:
    print('Invalid input,please enter all details in correct format')
