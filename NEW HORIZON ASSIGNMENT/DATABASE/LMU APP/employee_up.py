import re
import sqlite3


class EUF:
    def __init__(self, s_id, f_name, l_name, age, gender, salary, department, designation):
        self.st_id = s_id
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender
        self.salary = salary
        self.department = department
        self.designation = designation

    def first_name(self, stu_id, fi_name):
        self.st_id = stu_id
        self.f_name = fi_name

        conn = sqlite3.connect("Learn_More_University.db")

        try:

            cursor = conn.cursor()

            lst = []

            viewquery = "SELECT employeeID FROM Employee"

            result_viewquery = cursor.execute(viewquery)
            conn.commit()

            for i in result_viewquery:
                for j in i:
                    regex = re.findall("\d{7}[A-Z]{2,3}", j)
                    for k in regex:
                        x = k[:9]
                        lst.append(x)

                for s_id in lst:
                    if self.st_id == s_id:

                        updatestudentquery = "UPDATE Employee SET first_name ='" + self.f_name + "' WHERE employeeID ='" + self.st_id + "' "

                        cursor.execute(updatestudentquery)
                        conn.commit()

        except sqlite3.Error as e:
            print("SQLite error:", e)
            conn.rollback()

        finally:
            conn.close()

    def last_name(self, stu_id, la_name):
        self.st_id = stu_id
        self.l_name = la_name

        conn = sqlite3.connect("Learn_More_University.db")

        try:

            cursor = conn.cursor()

            lst = []

            viewquery = "SELECT employeeID FROM Employee"

            result_viewquery = cursor.execute(viewquery)
            conn.commit()

            for i in result_viewquery:
                for j in i:
                    regex = re.findall("\d{7}[A-Z]{2,3}", j)
                    for k in regex:
                        x = k[:9]
                        lst.append(x)

                for s_id in lst:
                    if self.st_id == s_id:

                        updatestudentquery = "UPDATE Employee SET last_name ='" + self.l_name + "' WHERE employeeID ='" + self.st_id + "' "

                        cursor.execute(updatestudentquery)
                        conn.commit()

        except sqlite3.Error as e:
            print("SQLite error:", e)
            conn.rollback()

        finally:
            conn.close()

    def age(self, stu_id, age):
        self.st_id = stu_id
        self.age = age

        conn = sqlite3.connect("Learn_More_University.db")

        try:

            cursor = conn.cursor()

            lst = []

            viewquery = "SELECT employeeID FROM Employee"

            result_viewquery = cursor.execute(viewquery)
            conn.commit()

            for i in result_viewquery:
                for j in i:
                    regex = re.findall("\d{7}[A-Z]{2,3}", j)
                    for k in regex:
                        x = k[:9]
                        lst.append(x)

                for s_id in lst:
                    if self.st_id == s_id:

                        updatestudentquery = "UPDATE Employee SET age ='" + self.age + "' WHERE employeeID ='" + self.st_id + "' "

                        cursor.execute(updatestudentquery)
                        conn.commit()

        except sqlite3.Error as e:
            print("SQLite error:", e)
            conn.rollback()

        finally:
            conn.close()

    def gender(self, stu_id, gen):
        self.st_id = stu_id
        self.gen = gen

        conn = sqlite3.connect("Learn_More_University.db")

        try:

            cursor = conn.cursor()

            lst = []

            viewquery = "SELECT employeeID FROM Employee"

            result_viewquery = cursor.execute(viewquery)
            conn.commit()

            for i in result_viewquery:
                for j in i:
                    regex = re.findall("\d{7}[A-Z]{2,3}", j)
                    for k in regex:
                        x = k[:9]
                        lst.append(x)

                for s_id in lst:
                    if self.st_id == s_id:

                        updatestudentquery = "UPDATE Employee SET gender ='" + self.gen + "' WHERE employeeID ='" + self.st_id + "' "

                        cursor.execute(updatestudentquery)
                        conn.commit()

        except sqlite3.Error as e:
            print("SQLite error:", e)
            conn.rollback()

        finally:
            conn.close()

    def salary(self, stu_id, sal):
        self.st_id = stu_id
        self.salary = sal

        conn = sqlite3.connect("Learn_More_University.db")

        try:

            cursor = conn.cursor()

            lst = []

            viewquery = "SELECT employeeID FROM Employee"

            result_viewquery = cursor.execute(viewquery)
            conn.commit()

            for i in result_viewquery:
                for j in i:
                    regex = re.findall("\d{7}[A-Z]{2,3}", j)
                    for k in regex:
                        x = k[:9]
                        lst.append(x)

                for s_id in lst:
                    if self.st_id == s_id:

                        updatestudentquery = "UPDATE Employee SET salary ='" + self.salary + "' WHERE employeeID ='" + self.st_id + "' "

                        cursor.execute(updatestudentquery)
                        conn.commit()

        except sqlite3.Error as e:
            print("SQLite error:", e)
            conn.rollback()

        finally:
            conn.close()

    def department(self, stu_id, dep):
        self.st_id = stu_id
        self.department = dep

        conn = sqlite3.connect("Learn_More_University.db")

        try:

            cursor = conn.cursor()

            lst = []

            viewquery = "SELECT employeeID FROM Employee"

            result_viewquery = cursor.execute(viewquery)
            conn.commit()

            for i in result_viewquery:
                for j in i:
                    regex = re.findall("\d{7}[A-Z]{2,3}", j)
                    for k in regex:
                        x = k[:9]
                        lst.append(x)

                for s_id in lst:
                    if self.st_id == s_id:

                        updatestudentquery = "UPDATE Employee SET department ='" + self.department + "' WHERE employeeID ='" + self.st_id + "' "

                        cursor.execute(updatestudentquery)
                        conn.commit()

        except sqlite3.Error as e:
            print("SQLite error:", e)
            conn.rollback()

        finally:
            conn.close()

    def designation(self, stu_id, desig):
        self.st_id = stu_id
        self.designation = desig

        conn = sqlite3.connect("Learn_More_University.db")

        try:

            cursor = conn.cursor()

            lst = []

            viewquery = "SELECT employeeID FROM Employee"

            result_viewquery = cursor.execute(viewquery)
            conn.commit()

            for i in result_viewquery:
                for j in i:
                    regex = re.findall("\d{7}[A-Z]{2,3}", j)
                    for k in regex:
                        x = k[:9]
                        lst.append(x)

                for s_id in lst:
                    if self.st_id == s_id:

                        updatestudentquery = "UPDATE Employee SET designation ='" + self.designation + "' WHERE employeeID ='" + self.st_id + "' "

                        cursor.execute(updatestudentquery)
                        conn.commit()

        except sqlite3.Error as e:
            print("SQLite error:", e)
            conn.rollback()

        finally:
            conn.close()
