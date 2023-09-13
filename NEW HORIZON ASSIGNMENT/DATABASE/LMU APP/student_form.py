import random
import string
import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import sqlite3


# create an instance for the entry form for the user
ue = Tk()
ue.config(bg="white")
ue.title("Student-Form")

msg_wid = 600
msg_hig = 720
scrn_wid = ue.winfo_screenwidth()
scrn_hig = ue.winfo_screenheight()
x_axis = (scrn_wid - msg_wid) // 2
y_axis = (scrn_hig - msg_hig) // 2
ue.geometry(f"{msg_wid}x{msg_hig}+{x_axis}+{y_axis}")
pic = PhotoImage(file="lmu_logo.png")
ue.iconphoto(False, pic)
image = Image.open("b3.jpg")
image = image.resize((msg_wid, msg_hig))
background_image = ImageTk.PhotoImage(image)
ue_label = Label(ue, image=background_image)
ue_label.pack()


class SF(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.student_form()

    # display an entry form when an "add student file is clicked" is selected
    def student_form(self):

        self.s_id_entry = StringVar()
        self.s_fn_entry = StringVar()
        self.s_ln_entry = StringVar()
        self.s_age_entry = IntVar()
        self.s_gender = StringVar()
        self.s_combo_course = StringVar()

        # get the value that the user selects
        self.sd_label = Label(ue, text="STUDENT ID:", font=("Calibri", 13, "bold"), bg="black", fg="white")
        self.sd_label.place(x=210, y=180)
        # condition statement for further processing
        self.value1 = self.random_student_id()
        self.sd = Label(ue, text="STUDENT ENTRY", font=("Calibri", 30, "bold", "italic"), bg="white", fg="black")
        self.sd.place(x=170, y=100)
        self.sd_label.config(text=f"STUDENT ID: {self.value1}")
        self.si_label = Label(ue, text="STUDENT ID:", font=("Calibri", 13, "bold"), bg="white", fg="black")
        self.si_label.place(x=150, y=240)
        self.si_entry = Entry(ue, textvariable=self.s_id_entry, font=("Calibri", 13))
        self.si_entry.place(x=280, y=240)
        self.sfn_label = Label(ue, text="FIRST NAME:", font=("Calibri", 13, "bold"), bg="white", fg="black")
        self.sfn_label.place(x=150, y=300)
        self.sfn_entry = Entry(ue, textvariable=self.s_fn_entry, font=("Calibri", 13))
        self.sfn_entry.place(x=280, y=300)
        self.sln_label = Label(ue, text="LAST NAME:", font=("Calibri", 13, "bold"), bg="white", fg="black")
        self.sln_label.place(x=150, y=360)
        self.sln_entry = Entry(ue, textvariable=self.s_ln_entry, font=("Calibri", 13))
        self.sln_entry.place(x=280, y=360)
        self.sa_label = Label(ue, text="AGE:", font=("Calibri", 13, "bold"), bg="white", fg="black")
        self.sa_label.place(x=150, y=420)
        self.sa_entry = Entry(ue, textvariable=self.s_age_entry, font=("Calibri", 13))
        self.sa_entry.place(x=280, y=420)
        self.sa_entry.delete(0, END)
        self.s_gender_label = Label(ue, text="GENDER:", font=("Calibri", 13, "bold"), bg="white", fg="black")
        self.s_gender_label.place(x=150, y=480)
        self.s_male_gender = Radiobutton(ue, variable=self.s_gender, text="Male", value="Male", font=("Calibri", 13, "bold"))
        self.s_male_gender.place(x=280, y=480)
        self.s_male_gender.select()
        self.s_female_gender = Radiobutton(ue, variable=self.s_gender, text="Female", value="Female", font=("Calibri", 13, "bold"))
        self.s_female_gender.place(x=380, y=480)
        self.s_course_label = Label(ue, text="COURSE ENROLLED:", font=("Calibri", 13, "bold"), bg="white", fg="black")
        self.s_course_label.place(x=150, y=540)
        self.s_course_combo = Combobox(ue, textvariable=self.s_combo_course, values=("Accounting", "Anatomy", "Animal-husbandry", "Business-Administration", "Bio-chemistry", "Chemistry", "Child-Education", "Civil-Engineering", "Computer-Engineering", "Computer-Science", "Economics", "Electrical-Engineering", "English-And-Literary-Studies", "Finance", "History", "Human-Kinetics", "Industrial-Chemistry", "International-Relations-And-Project-Management", "Law", "Linguistics", "Mass-Communication", "Mathematics", "Mechanical-Engineering", "Medicine-And-Surgery", "Microbiology", "Physics", "Physiology", "Plant-Science", "Soil-Science", "Theatre-And-Media-Arts", "Vocational-Education"), font=("Calibri", 13, "bold"), width=19)
        self.s_course_combo.place(x=310, y=540)
        self.s_save_btn = Button(ue, text="Save", font=("Arial", 21, "bold"), bg="orangered", fg="black", activebackground="orangered", relief="flat", command=self.save_student)
        self.s_save_btn.place(x=250, y=600)

    # generate a student ID
    def random_student_id(self):
        self.letters = string.ascii_letters.upper()
        self.random_letters = [random.choice(self.letters) for i in range(2)]
        self.ran = ''.join(self.random_letters)
        self.number_list = []
        k = 1
        while k <= 7:
            self.number = random.randint(0, 9)
            self.number_list.append(self.number)
            k += 1
        s = [str(i) for i in self.number_list]
        self.res = (''.join(s))
        self.val = self.res + self.ran
        print("STUDENT ID:", self.val)
        return self.val

    # define a function to save student information
    def save_student(self):
        self.ssid = self.si_entry.get().upper()
        self.ssfn = self.sfn_entry.get().upper()
        self.ssln = self.sln_entry.get().upper()
        try:
            self.ssa = str(self.sa_entry.get())
        except:
            messagebox.showwarning("Error", "Enter age in digits")
        self.ssg = self.s_gender.get().upper()
        self.ssc = self.s_course_combo.get().upper()
        self.date = time.ctime()

        # condition for processing
        if self.ssid == self.value1 and self.ssa and self.ssg and self.ssc:
            conn = sqlite3.connect("Learn_More_University.db")

            try:
                cursor = conn.cursor()

                insert_student_query = "INSERT INTO Students (studentID, first_name, last_name, age, gender, course) VALUES (?, ?, ?, ?, ?, ?)"

                cursor.execute(insert_student_query, (self.ssid, self.ssfn, self.ssln, self.ssa, self.ssg, self.ssc))
                conn.commit()
                messagebox.showinfo("Success", "Info added successfully")
                ue.destroy()

            except sqlite3.Error as e:
                messagebox.showerror("Error", "Info not successfully added")
                print("SQLite error:", e)
                conn.rollback()

            finally:
                conn.close()
                from learn_more_uni import main_lmu_app

        else:
            messagebox.showwarning("Error", "Invalid Student ID")

    # function to close student form and entry
    def close_student(self):
        ue.destroy()


stu_form = SF(ue)
stu_form.mainloop()
