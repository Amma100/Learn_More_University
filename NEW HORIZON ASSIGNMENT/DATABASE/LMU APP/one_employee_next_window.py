import re
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3


emp = Tk()
emp.config(bg="white")
emp.title("Employee-File-Search")
msg_wid = 500
msg_hig = 150
scrn_wid = emp.winfo_screenwidth()
scrn_hig = emp.winfo_screenheight()
x_axis = (scrn_wid - msg_wid) // 2
y_axis = (scrn_hig - msg_hig) // 2
emp.geometry(f"{msg_wid}x{msg_hig}+{x_axis}+{y_axis}")
pic = PhotoImage(file="lmu_logo.png")
emp.iconphoto(False, pic)
image = Image.open("b3.jpg")
image = image.resize((msg_wid, msg_hig))
background_image = ImageTk.PhotoImage(image)
stu_label = Label(emp, image=background_image)
stu_label.pack()


class OEN(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.one_employee_next()

    def one_employee_next(self):
        self.emp_entry = StringVar()

        self.emid_label = Label(emp, text="EMPLOYEE ID:", font=("Calibri", 13, "bold"), bg="white", fg="black")
        self.emid_label.place(x=30, y=80)
        self.emid_entry = Entry(emp, textvariable=self.emp_entry, font=("Calibri", 13))
        self.emid_entry.place(x=160, y=80)
        self.emclose_btn = Button(emp, text="VIEW", font=("Arial", 13, "bold"), bg="orangered", fg="black", activebackground="orangered", relief="flat", command=self.employee_view)
        self.emclose_btn.place(x=365, y=80)

    # view employee ID
    def employee_view(self):
        self.value_emp = self.emid_entry.get().upper()

        self.wrong_employee_id = ""

        if self.value_emp == self.wrong_employee_id:
            messagebox.showwarning("Error", "Please enter Employee ID")

        else:
            if self.value_emp != "":

                conn = sqlite3.connect("Learn_More_University.db")

                try:

                    cursor = conn.cursor()

                    lst = []

                    viewquery = "SELECT employeeID FROM Employee"

                    result_viewquery = cursor.execute(viewquery)
                    conn.commit()

                    for i in result_viewquery:
                        for j in i:
                            regex = re.findall("\d{4}[A-Z]{2,3}", j)
                            for k in regex:
                                x = k[:9]
                                lst.append(x)

                        for e_id in lst:
                            if self.value_emp == e_id:
                                emp.destroy()

                                self.ev = Tk()
                                self.ev.title("Employee")
                                self.msg_wid = 600
                                self.msg_hig = 400
                                self.scrn_wid = self.ev.winfo_screenwidth()
                                self.scrn_hig = self.ev.winfo_screenheight()
                                self.x_axis = (self.scrn_wid - self.msg_wid) // 2
                                self.y_axis = (self.scrn_hig - self.msg_hig) // 2
                                self.ev.geometry(f"{self.msg_wid}x{self.msg_hig}+{self.x_axis}+{self.y_axis}")
                                self.pic = PhotoImage(file="lmu_logo.png")
                                self.ev.iconphoto(False, self.pic)
                                self.image = Image.open("b3.jpg")
                                self.image = self.image.resize((self.msg_wid, self.msg_hig))
                                self.background_image = ImageTk.PhotoImage(self.image)
                                self.ev_label = Label(self.ev, image=self.background_image)
                                self.ev_label.pack()

                                viewemployeequery = "SELECT employeeID, first_name, last_name, age, gender, salary, department, designation FROM Employee WHERE employeeID ='" + self.value_emp + "' "

                                result = cursor.execute(viewemployeequery)
                                conn.commit()

                                for i in result:
                                    self.ev_name_label = Label(self.ev, text=f"{i[1]} {i[2]} DETAILS", font=("Calibri", 20, "bold"), bg="white", fg="black")
                                    self.ev_name_label.place(x=100, y=10)
                                    self.ev_id_label = Label(self.ev, font=("Calibri", 16, "bold"), bg="white", fg="black")
                                    self.ev_id_label.place(x=100, y=80)
                                    self.ev_id_label.config(text=f"Employee ID: {i[0]}")
                                    self.ev_first_name_label = Label(self.ev, font=("Calibri", 16, "bold"), bg="white", fg="black")
                                    self.ev_first_name_label.place(x=100, y=110)
                                    self.ev_first_name_label.config(text=f"FIRST NAME: {i[1]}")
                                    self.ev_last_name_label = Label(self.ev, font=("Calibri", 16, "bold"), bg="white", fg="black")
                                    self.ev_last_name_label.place(x=100, y=140)
                                    self.ev_last_name_label.config(text=f"LAST NAME: {i[2]}")
                                    self.ev_age_label = Label(self.ev, font=("Calibri", 16, "bold"), bg="white", fg="black")
                                    self.ev_age_label.place(x=100, y=170)
                                    self.ev_age_label.config(text=f"AGE: {i[3]}")
                                    self.ev_gender_label = Label(self.ev, font=("Calibri", 16, "bold"), bg="white", fg="black")
                                    self.ev_gender_label.place(x=100, y=200)
                                    self.ev_gender_label.config(text=f"GENDER: {i[4]}")
                                    self.ev_course_label = Label(self.ev, font=("Calibri", 16, "bold"), bg="white", fg="black")
                                    self.ev_course_label.place(x=100, y=230)
                                    self.ev_course_label.config(text=f"SALARY: {i[5]}")
                                    self.ev_department_label = Label(self.ev, font=("Calibri", 16, "bold"), bg="white", fg="black")
                                    self.ev_department_label.place(x=100, y=260)
                                    self.ev_department_label.config(text=f"DEPARTMENT NAME: {i[6]}")
                                    self.ev_designation_label = Label(self.ev, font=("Calibri", 16, "bold"), bg="white", fg="black")
                                    self.ev_designation_label.place(x=100, y=290)
                                    self.ev_designation_label.config(text=f"DESIGNATION: {i[7]}")
                                    self.ev_close = Button(self.ev, text="CLOSE", font=("Arial", 13, "bold"), bg="orangered", fg="black", activebackground="orangered", relief="flat", command=self.close_employee_view)
                                    self.ev_close.place(x=255, y=350)

                                self.ev.mainloop()

                except sqlite3.Error as e:
                    print("SQLite error:", e)
                    messagebox.showerror("Error", "Employee ID is invalid")
                    conn.rollback()

                finally:
                    conn.close()

    # function to close one employee ID
    def close_employee_view(self):
        self.ev.destroy()


oen_app = OEN(emp)
oen_app.mainloop()

