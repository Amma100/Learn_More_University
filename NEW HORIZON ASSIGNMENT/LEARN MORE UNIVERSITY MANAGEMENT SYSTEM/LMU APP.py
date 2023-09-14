from display_module import *
from info_module import *
from management_module import *

display()
welcome()
while True:
    details()
    try:
        # get user response for option above
        val = int(input("\nEnter a value: "))
        # perform some functions if user enters 1
        if val == 1:
            display()
            # collect student full name, age, gender, course enrolled and student ID
            while True:
                value_1 = input("\nAdd Student data(y/n): ")
                if value_1 == "y":
                    student_entry()
                    S = random_student_id()
                    while True:
                        Student_id = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Enter student ID: ").upper()
                        if Student_id != S or Student_id == "":
                            print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t ---Error message: Invalid Student ID---")
                        if Student_id == S:
                            break
                    First_name = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Enter first name: ").upper()
                    Last_name = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Enter last name: ").upper()
                    Age = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Enter age: ")
                    Gender = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Enter gender: ").upper()
                    Course_enrolled = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Enter course enrolled: ").upper()
                    tm = time.ctime()
                    Student = Student_Info(First_name, Last_name, Age, Gender, Course_enrolled, Student_id)
                    student_data(First_name, Last_name, Age, Gender, Course_enrolled, Student_id, tm)
                    student_data_backup(Student_id)
                if value_1 == "n":
                    break
        # perform some functions if user enters 2
        if val == 2:
            display()
            # collect employee full name, age, gender, salary, department name, designation and employee ID
            while True:
                value_2 = input("\nAdd prisoner data(y/n): ")
                if value_2 == "y":
                    employee_entry()
                    E = random_employee_id()
                    Employee_id = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Enter Employee ID: ").upper()
                    while True:
                        if Employee_id != E or Employee_id == "":
                            print("---Error message: Invalid Employee ID---")
                        else:
                            break
                    First_name = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Enter first name: ").upper()
                    Last_name = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Enter last name: ").upper()
                    Age = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Enter age: ")
                    Gender = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Enter gender: ").upper()
                    Salary = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Enter salary: ")
                    Department_name = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Enter department name: ").upper()
                    Designation = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Enter designation: ").upper()
                    tm = time.ctime()
                    Employee = Employee_Info(First_name, Last_name, Age, Gender, Salary, Department_name, Designation,
                                             Employee_id)
                    employee_data(First_name, Last_name, Age, Gender, Salary, Department_name, Designation, Employee_id,
                                  tm)
                    employee_data_backup(Employee_id)
                if value_2 == "n":
                    break
        # perform some functions if user enters 3
        if val == 3:
            display()
            # display student full name, age, gender, course enrolled and student ID
            view_data()
            try:
                # get user response for option above
                val3 = int(input("\nEnter a value: "))
                if val3 == 1:
                    display()
                    while True:
                        view_student_data()
                        try:
                            val3_1 = int(input("Enter a value: "))
                            if val3_1 == 1:
                                display()
                                view_student_id()
                                print("\n")
                                one_student_data()
                                break
                            if val3_1 == 2:
                                display()
                                view_all_student_data()
                                print("\n")
                                all_students_data()
                                break
                        except:
                            print("---Error message: Invalid number---")
                if val3 == 2:
                    display()
                    while True:
                        view_employee_data()
                        try:
                            val3_2 = int(input("Enter a value: "))
                            if val3_2 == 1:
                                display()
                                view_employee_id()
                                print("\n")
                                one_employee_data()
                                break
                            if val3_2 == 2:
                                display()
                                view_all_employee_data()
                                print("\n")
                                all_employees_data()
                                break
                        except:
                            print("---Error message: Invalid number---")
            except:
                print("---Error message: Invalid number---")
        # perform some functions if user enters 4
        if val == 4:
            exit()
    except:
        print("---Invalid Entry---")
