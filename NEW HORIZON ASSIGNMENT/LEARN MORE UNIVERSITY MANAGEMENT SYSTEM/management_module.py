"""
These functions will collect, store, update and retrieve students records and information
"""
import os
import random
import string
import time


########################################################################################################################
def random_student_id():
    letters = string.ascii_letters.upper()
    random_letters = [random.choice(letters) for i in range(2)]
    ran = ''.join(random_letters)
    number_list = []
    k = 1
    while k <= 7:
        number = random.randint(0, 9)
        number_list.append(number)
        k += 1
    s = [str(i) for i in number_list]
    res = (''.join(s))
    val = res + ran
    print("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tSTUDENT ID:", val)
    return val


def random_employee_id():
    letters = string.ascii_letters.upper()
    random_letters = [random.choice(letters) for i in range(2)]
    ran = ''.join(random_letters)
    number_list = []
    k = 1
    while k <= 4:
        number = random.randint(0, 9)
        number_list.append(number)
        k += 1
    s = [str(i) for i in number_list]
    res = (''.join(s))
    val = res + ran
    print("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEMPLOYEE ID:", val)
    return val


########################################################################################################################
def student_data(first_name, last_name, age, gender, course_enrolled, student_id, tm):
    if os.path.isfile("student.txt") is False:
        print("\n---Can't write to Student.txt, file not found---")
    else:
        file_handle = open("student.txt", "a")

        file_handle.write("\n")
        file_handle.write(student_id)
        file_handle.write("\t\t\t\t")
        file_handle.write(first_name)
        file_handle.write("\t\t\t\t\t\t\t\t\t\t\t\t\t ")
        file_handle.write(last_name)
        file_handle.write("\t\t\t\t\t\t\t\t\t\t\t\t\t ")
        file_handle.write(age)
        file_handle.write("\t\t\t")
        file_handle.write(gender)
        file_handle.write("\t\t\t\t")
        file_handle.write("({})".format(course_enrolled))
        file_handle.write("\t\t\t")
        file_handle.write("({})".format(tm))
        file_handle.write("\n")

        print("\n\n---File updated successfully---")
        file_handle.close()
    date = time.ctime()
    print("\nFile updated at", date)


# backup students data
def student_data_backup(student_id):
    if os.path.isfile("student.txt") is False:
        print("\n---Can't write to Student.txt, file not found---")
    else:
        file_handle = open("student.txt", "r")
        for i in file_handle:
            if not i.startswith(student_id):
                continue
            result = "".join(i)
            if os.path.isfile("student_backup.txt") is False:
                print("\n---Can't write to Student_backup.txt, file not found---")
            else:
                file_handle = open("student_backup.txt", "a")

                file_handle.write("\n")
                file_handle.write(result)
                file_handle.write("\n")

                file_handle.close()


# view all students data when query is sent
def all_students_data():
    if os.path.isfile("student.txt") is False:
        print("\n---Can't write to Student.txt, file not found---")
    else:
        file_handle = open("student.txt", "r")
        for i in file_handle:
            result = i.split()
            if result:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t{} {} DETAILS".format(result[1], result[2]))
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t=======================\n")
                print(
                    "[STUDENT ID: {}, FIRST NAME: {}, LAST NAME: {}, AGE: {}, GENDER: {}, COURSE ENROLLED: {}]".format(
                        result[0], result[1], result[2], result[3], result[4], result[5]))
        file_handle.close()
    date = time.ctime()
    print("\nFile viewed at", date)


# view one student data when query is sent
def one_student_data():
    wrong_student_id = ""
    student_id = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter student ID: ").upper()
    if student_id == wrong_student_id:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t ---Error message: Invalid Student ID---")
        return one_student_data()

    if os.path.isfile("student.txt") is True:
        file_handle = open("student.txt", "r")
        for i in file_handle:
            if i.startswith(student_id) is True:
                result = i.split()
                print("\n{} {} DETAILS".format(result[1], result[2]))
                print("=======================\n")
                print("Student ID: {}".format(result[0]))
                print("First Name: {}".format(result[1]))
                print("Last Name: {}".format(result[2]))
                print("Age: {}".format(result[3]))
                print("Gender: {}".format(result[4]))
                print("Course enrolled: {}".format(result[5]))
                print("=======================\n")


########################################################################################################################


########################################################################################################################
def employee_data(first_name, last_name, age, gender, salary, department_name, designation, employee_id, tm):
    if os.path.isfile("employee.txt") is False:
        print("\n---Can't write to Employee.txt, file not found---")
    else:
        file_handle = open("employee.txt", "a")

        file_handle.write("\n")
        file_handle.write(employee_id)
        file_handle.write("\t\t\t\t")
        file_handle.write(first_name)
        file_handle.write("\t\t\t\t\t\t\t\t\t\t\t\t\t ")
        file_handle.write(last_name)
        file_handle.write("\t\t\t\t\t\t\t\t\t\t\t\t\t ")
        file_handle.write(age)
        file_handle.write("\t\t\t")
        file_handle.write(gender)
        file_handle.write("\t\t\t\t")
        file_handle.write(salary)
        file_handle.write("\t\t\t")
        file_handle.write("({})".format(department_name))
        file_handle.write("\t\t\t\t")
        file_handle.write("({})".format(designation))
        file_handle.write("\t\t\t\t")
        file_handle.write("({})".format(tm))
        file_handle.write("\n")

        print("\n\n---File updated successfully---")
        file_handle.close()
    date = time.ctime()
    print("\nFile updated at", date)


# backup employees data
def employee_data_backup(employee_id):
    if os.path.isfile("employee.txt") is False:
        print("\n---Can't write to Employee.txt, file not found---")
    else:
        file_handle = open("employee.txt", "r")
        for i in file_handle:
            if not i.startswith(employee_id):
                continue
            result = "".join(i)
            if os.path.isfile("employee_backup.txt") is False:
                print("\n---Can't write to Employee_backup.txt, file not found---")
            else:
                file_handle = open("employee_backup.txt", "a")

                file_handle.write("\n")
                file_handle.write(result)
                file_handle.write("\n")

                file_handle.close()


# view all employees data when query is sent
def all_employees_data():
    if os.path.isfile("employee.txt") is False:
        print("\n---Can't write to Student.txt, file not found---")
    else:
        file_handle = open("employee.txt", "r")
        for i in file_handle:
            result = i.split()
            if result:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t{} {} DETAILS".format(result[1], result[2]))
                print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t=======================\n")
                print(
                    "[EMPLOYEE ID: {}, FIRST NAME: {}, LAST NAME: {}, AGE: {}, GENDER: {}, SALARY: {}, DEPARTMENT NAME: {}, DESIGNATION: {}]".format(
                        result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7]))
        file_handle.close()
    date = time.ctime()
    print("\nFile viewed at", date)


# view one employee data when query is sent
def one_employee_data():
    wrong_employee_id = ""
    employee_id = input("\n    \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter employee ID: ").upper()
    if employee_id == wrong_employee_id:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t ---Error message: Invalid Employee ID---")
        return one_employee_data()

    if os.path.isfile("employee.txt") is True:
        file_handle = open("employee.txt", "r")
        for i in file_handle:
            if i.startswith(employee_id) is True:
                result = i.split()
                print("\n{} {} DETAILS".format(result[1], result[2]))
                print("=======================\n")
                print("Teacher ID: {}".format(result[0]))
                print("First Name: {}".format(result[1]))
                print("Last Name: {}".format(result[2]))
                print("Age: {}".format(result[3]))
                print("Gender: {}".format(result[4]))
                print("Salary: {}".format(result[5]))
                print("Department_name: {}".format(result[6]))
                print("Designation: {}".format(result[7]))
########################################################################################################################
