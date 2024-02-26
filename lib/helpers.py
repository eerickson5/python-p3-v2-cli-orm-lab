from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    for empl in Employee.get_all():
        print(empl)


def find_employee_by_name():
    name = input("Search Name: ")
    empl = find_employee_by_name(name)
    print(empl) if empl else print(f"No employee {name} found.")



def find_employee_by_id():
    _id = input("Search ID: ")
    empl = find_department_by_id(_id)
    print(empl) if empl else print (f"No employee with ID {_id} found.")


def create_employee():
    name = input("Employee Name: ")
    job = input("Job Title: ")
    department = input("Department ID: ")

    try:
        empl = Employee.create(name, job, department)
        print(f"New Employee Born: {empl}")
    except Exception as exc:
        print(f"Error creating Employee {exc}")


def update_employee():
    _id = input("Employee ID: ")
    if(empl := Employee.find_by_id(_id)):
        try:
            name = input("Employee Name: ")
            empl.name = name
            job = input("Job Title: ")
            empl.job_title = job
            depo = input("Department ID: ")
            empl.department_id = depo
        except Exception as exc:
            print(exc)
        empl.update()
        print(f"Employee: {empl}")
    else:
        print("Employee does not exist.")


def delete_employee():
    _id = input("Employee ID: ")
    if empl := Employee.find_by_id(_id):
        empl.delete()
        print(f'Employee {_id} deleted')
    else:
        print(f"Employee {_id} not found")


def list_department_employees():
    depo_id = input("Department ID: ")
    depo = Department.find_by_id(depo_id)
    if depo:
        for empl in depo.employees():
            print(empl.name)
    else:
        print("Department not found.")