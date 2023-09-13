import re
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3


stu = Tk()
stu.config(bg="white")
stu.title("Student-File")
msg_wid = 500
msg_hig = 150
scrn_wid = stu.winfo_screenwidth()
scrn_hig = stu.winfo_screenheight()
x_axis = (scrn_wid - msg_wid) // 2
y_axis = (scrn_hig - msg_hig) // 2
stu.geometry(f"{msg_wid}x{msg_hig}+{x_axis}+{y_axis}")
pic = PhotoImage(file="lmu_logo.png")
stu.iconphoto(False, pic)
image = Image.open("b3.jpg")
image = image.resize((msg_wid, msg_hig))
background_image = ImageTk.PhotoImage(image)
stu_label = Label(stu, image=background_image)
stu_label.pack()


class OSN(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.one_student_next()

    def one_student_next(self):
        self.stu_entry = StringVar()

        self.esid_label = Label(stu, text="STUDENT ID:", font=("Calibri", 13, "bold"), bg="white", fg="black")
        self.esid_label.place(x=30, y=80)
        self.esid_entry = Entry(stu, textvariable=self.stu_entry, font=("Calibri", 13))
        self.esid_entry.place(x=140, y=80)
        self.eclose_btn = Button(stu, text="VIEW", font=("Arial", 13, "bold"), bg="orangered", fg="black", activebackground="orangered", relief="flat", command=self.student_view)
        self.eclose_btn.place(x=365, y=80)

    # view student ID
    def student_view(self):
        self.value_stu = self.esid_entry.get().upper()

        self.wrong_student_id = ""

        if self.value_stu == self.wrong_student_id:
            messagebox.showwarning("Error", "Please enter Student ID")

        else:
            if self.value_stu != "":
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
                            if self.value_stu == s_id:
                                stu.destroy()

                                self.sv = Tk()
                                self.sv.title("Student")
                                self.msg_wid = 600
                                self.msg_hig = 350
                                self.scrn_wid = self.sv.winfo_screenwidth()
                                self.scrn_hig = self.sv.winfo_screenheight()
                                self.x_axis = (self.scrn_wid - self.msg_wid) // 2
                                self.y_axis = (self.scrn_hig - self.msg_hig) // 2
                                self.sv.geometry(f"{self.msg_wid}x{self.msg_hig}+{self.x_axis}+{self.y_axis}")
                                self.pic = PhotoImage(file="lmu_logo.png")
                                self.sv.iconphoto(False, self.pic)
                                self.image = Image.open("b3.jpg")
                                self.image = self.image.resize((self.msg_wid, self.msg_hig))
                                self.background_image = ImageTk.PhotoImage(self.image)
                                self.sv_label = Label(self.sv, image=self.background_image)
                                self.sv_label.pack()

                                viewstudentquery = "SELECT studentID, first_name, last_name, age, gender, course FROM Students WHERE studentID ='" + self.value_stu + "' "

                                result = cursor.execute(viewstudentquery)
                                conn.commit()

                                for id in result:
                                    self.sv_name_label = Label(self.sv, text=f"{id[1]} {id[2]} DETAILS", font=("Calibri", 20, "bold"), bg="white", fg="black")
                                    self.sv_name_label.place(x=100, y=10)
                                    self.sv_id_label = Label(self.sv, font=("Calibri", 16, "bold"), bg="white", fg="black")
                                    self.sv_id_label.place(x=100, y=80)
                                    self.sv_id_label.config(text=f"Student ID: {id[0]}")
                                    self.sv_first_name_label = Label(self.sv, font=("Calibri", 16, "bold"), bg="white", fg="black")
                                    self.sv_first_name_label.place(x=100, y=110)
                                    self.sv_first_name_label.config(text=f"FIRST NAME: {id[1]}")
                                    self.sv_last_name_label = Label(self.sv, font=("Calibri", 16, "bold"), bg="white", fg="black")
                                    self.sv_last_name_label.place(x=100, y=140)
                                    self.sv_last_name_label.config(text=f"LAST NAME: {id[2]}")
                                    self.sv_age_label = Label(self.sv, font=("Calibri", 16, "bold"), bg="white", fg="black")
                                    self.sv_age_label.place(x=100, y=170)
                                    self.sv_age_label.config(text=f"AGE: {id[3]}")
                                    self.sv_gender_label = Label(self.sv, font=("Calibri", 16, "bold"), bg="white", fg="black")
                                    self.sv_gender_label.place(x=100, y=200)
                                    self.sv_gender_label.config(text=f"GENDER: {id[4]}")
                                    self.sv_course_label = Label(self.sv, font=("Calibri", 16, "bold"), bg="white", fg="black")
                                    self.sv_course_label.place(x=100, y=230)
                                    self.sv_course_label.config(text=f"COURSE ENROLLED: {id[5]}")
                                    self.sv_close = Button(self.sv, text="CLOSE", font=("Arial", 13, "bold"), bg="orangered", fg="black", activebackground="orangered", relief="flat", command=self.close_student_view)
                                    self.sv_close.place(x=255, y=300)

                                self.sv.mainloop()

                except sqlite3.Error as e:
                    print("SQLite error:", e)
                    messagebox.showerror("Error", "Student ID is invalid")
                    conn.rollback()

                finally:
                    conn.close()

    # function to close one student ID
    def close_student_view(self):
        self.sv.destroy()


osn_app = OSN(stu)
osn_app.mainloop()
