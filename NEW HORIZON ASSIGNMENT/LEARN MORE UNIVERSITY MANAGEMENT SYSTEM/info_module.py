"""
This code will contain the parent class that is going to be inherited.
Students details and Teachers details will share some common attributes
"""


# general class inheritance
class General_Info:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender


class Student_Info(General_Info):
    def __init__(self, first_name, last_name, age, gender, course_enrolled, student_id):
        super().__init__(first_name, last_name, age, gender)
        self.course_enrolled = course_enrolled
        self.student_id = student_id

    # Define Setter and Getter method for student
    def set_student_first_name(self, f_name):
        self.first_name = f_name

    def get_student_first_name(self):
        return self.first_name

    def set_student_last_name(self, l_name):
        self.last_name = l_name

    def get_student_last_name(self):
        return self.last_name

    def set_student_age(self, s_age):
        self.age = s_age

    def get_student_age(self):
        return self.age

    def set_student_gender(self, s_gender):
        self.gender = s_gender

    def get_student_gender(self):
        return self.gender

    def set_student_course_enrolled(self, s_course_enrolled):
        self.course_enrolled = s_course_enrolled

    def get_student_course_enrolled(self):
        return self.course_enrolled

    def get_student_id(self):
        return self.student_id

    # Property method
    s_f_name = property(get_student_first_name, set_student_first_name)
    s_l_name = property(get_student_last_name, set_student_last_name)
    s_age = property(get_student_age, set_student_age)
    s_gender = property(get_student_gender, set_student_gender)
    s_course_enrolled = property(get_student_course_enrolled, set_student_course_enrolled)
    s_id = property(get_student_id)


class Employee_Info(General_Info):
    def __init__(self, first_name, last_name, age, gender, salary, department_name, designation, employee_id):
        super().__init__(first_name, last_name, age, gender)
        self.salary = salary
        self.department_name = department_name
        self.designation = designation
        self.employee_id = employee_id

    # Define Setter and Getter method for student
    def set_employee_first_name(self, f_name):
        self.first_name = f_name

    def get_employee_first_name(self):
        return self.first_name

    def set_employee_last_name(self, l_name):
        self.last_name = l_name

    def get_employee_last_name(self):
        return self.last_name

    def set_employee_age(self, e_age):
        self.age = e_age

    def get_employee_age(self):
        return self.age

    def set_employee_gender(self, e_gender):
        self.gender = e_gender

    def get_employee_gender(self):
        return self.gender

    def set_employee_salary(self, e_salary):
        self.salary = e_salary

    def get_employee_salary(self):
        return self.salary

    def set_employee_department_name(self, e_department_name):
        self.department_name = e_department_name

    def get_employee_department_name(self):
        return self.department_name

    def set_employee_designation(self, e_designation):
        self.designation = e_designation

    def get_employee_designation(self):
        return self.designation

    def get_employee_id(self):
        return self.employee_id

    # Property method
    e_f_name = property(get_employee_first_name, set_employee_first_name)
    e_l_name = property(get_employee_last_name, set_employee_last_name)
    e_age = property(get_employee_age, set_employee_age)
    e_gender = property(get_employee_gender, set_employee_gender)
    e_salary = property(get_employee_salary, set_employee_salary)
    e_department_name = property(get_employee_department_name, set_employee_department_name)
    e_designation = property(get_employee_designation, set_employee_designation)
    e_id = property(get_employee_id)
