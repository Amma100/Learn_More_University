import re
import sqlite3


class SUF:
    def __init__(self, id, f_name, l_name, age, gender, course):
        self.st_id = id
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender
        self.course = course

    def first_name(self, stu_id, fi_name):
        self.st_id = stu_id
        self.f_name = fi_name

        conn = sqlite3.connect("Learn_More_University.db")

        try:

            cursor = conn.cursor()

            lst = []

            viewquery = "SELECT studentID FROM Students"

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

                        updatestudentquery = "UPDATE Students SET first_name ='" + self.f_name + "' WHERE studentID ='" + self.st_id + "' "

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

            viewquery = "SELECT studentID FROM Students"

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

                        updatestudentquery = "UPDATE Students SET last_name ='" + self.l_name + "' WHERE studentID ='" + self.st_id + "' "

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

            viewquery = "SELECT studentID FROM Students"

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

                        updatestudentquery = "UPDATE Students SET age ='" + self.age + "' WHERE studentID ='" + self.st_id + "' "

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

            viewquery = "SELECT studentID FROM Students"

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

                        updatestudentquery = "UPDATE Students SET gender ='" + self.gen + "' WHERE studentID ='" + self.st_id + "' "

                        cursor.execute(updatestudentquery)
                        conn.commit()

        except sqlite3.Error as e:
            print("SQLite error:", e)
            conn.rollback()

        finally:
            conn.close()

    def course(self, stu_id, co):
        self.st_id = stu_id
        self.course = co

        conn = sqlite3.connect("Learn_More_University.db")

        try:

            cursor = conn.cursor()

            lst = []

            viewquery = "SELECT studentID FROM Students"

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

                        updatestudentquery = "UPDATE Students SET course ='" + self.course + "' WHERE studentID ='" + self.st_id + "' "

                        cursor.execute(updatestudentquery)
                        conn.commit()

        except sqlite3.Error as e:
            print("SQLite error:", e)
            conn.rollback()

        finally:
            conn.close()
