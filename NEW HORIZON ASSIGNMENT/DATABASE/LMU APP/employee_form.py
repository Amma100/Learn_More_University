import random
import sqlite3
import string
import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk


# create an instance for the entry form for the user
ve = Tk()
ve.config(bg="white")
ve.title("Employee-Form")
msg_wid = 600
msg_hig = 720
scrn_wid = ve.winfo_screenwidth()
scrn_hig = ve.winfo_screenheight()
x_axis = (scrn_wid - msg_wid) // 2
y_axis = (scrn_hig - msg_hig) // 2
ve.geometry(f"{msg_wid}x{msg_hig}+{x_axis}+{y_axis}")
pic = PhotoImage(file="lmu_logo.png")
ve.iconphoto(False, pic)
image = Image.open("b3.jpg")
image = image.resize((msg_wid, msg_hig))
background_image = ImageTk.PhotoImage(image)
ue_label = Label(ve, image=background_image)
ue_label.pack()


class EF(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.employee_form()

    # display an entry form when an "add employee file is clicked" is selected
    def employee_form(self):


        self.e_id_entry = StringVar()
        self.e_fn_entry = StringVar()
        self.e_ln_entry = StringVar()
        self.e_age_entry = IntVar()
        self.e_gender1 = StringVar()
        self.e_dep_combo = StringVar()
        self.e_des_combo = StringVar()
        self.e_salary_entry = IntVar()

        # get the value that the user selects
        self.ed_label = Label(ve, text="EMPLOYEE ID:", font=("Calibri", 13, "bold"), bg="black", fg="white")
        self.ed_label.place(x=210, y=120)
        # condition statement for further processing
        self.value4 = self.random_employee_id()
        self.ed = Label(ve, text="EMPLOYEE ENTRY", font=("Calibri", 30, "bold", "italic"), bg="white", fg="black")
        self.ed.place(x=170, y=40)
        self.ed_label.config(text=f"EMPLOYEE ID: {self.value4}")
        self.ei_label = Label(ve, text="EMPLOYEE ID:", font=("Calibri", 13, "bold"), bg="white", fg="black")
        self.ei_label.place(x=150, y=180)
        self.ei_entry = Entry(ve, textvariable=self.e_id_entry, font=("Calibri", 13))
        self.ei_entry.place(x=280, y=180)
        self.efn_label = Label(ve, text="FIRST NAME:", font=("Calibri", 13, "bold"), bg="white", fg="black")
        self.efn_label.place(x=150, y=240)
        self.efn_entry = Entry(ve, textvariable=self.e_fn_entry, font=("Calibri", 13))
        self.efn_entry.place(x=280, y=240)
        self.eln_label = Label(ve, text="LAST NAME:", font=("Calibri", 13, "bold"), bg="white", fg="black")
        self.eln_label.place(x=150, y=300)
        self.eln_entry = Entry(ve, textvariable=self.e_ln_entry, font=("Calibri", 13))
        self.eln_entry.place(x=280, y=300)
        self.ea_label = Label(ve, text="AGE:", font=("Calibri", 13, "bold"), bg="white", fg="black")
        self.ea_label.place(x=150, y=360)
        self.ea_entry = Entry(ve, textvariable=self.e_age_entry, font=("Calibri", 13))
        self.ea_entry.place(x=280, y=360)
        self.ea_entry.delete(0, END)
        self.e_gender_label = Label(ve, text="GENDER:", font=("Calibri", 13, "bold"), bg="white", fg="black")
        self.e_gender_label.place(x=150, y=420)
        self.e_male_gender = Radiobutton(ve, variable=self.e_gender1, text="Male", value="Male", font=("Calibri", 13, "bold"))
        self.e_male_gender.place(x=280, y=420)
        self.e_male_gender.select()
        self.e_female_gender = Radiobutton(ve, variable=self.e_gender1, text="Female", value="Female", font=("Calibri", 13, "bold"))
        self.e_female_gender.place(x=380, y=420)
        self.e_salary_label = Label(ve, text="SALARY:", font=("Calibri", 13, "bold"), bg="white", fg="black")
        self.e_salary_label.place(x=150, y=480)
        self.e_sal_entry = Entry(ve, textvariable=self.e_salary_entry, font=("Calibri", 13))
        self.e_sal_entry.place(x=280, y=480)
        self.e_sal_entry.delete(0, END)
        self.e_dep_label = Label(ve, text="DEPARTMENT:", font=("Calibri", 13, "bold"), bg="white", fg="black")
        self.e_dep_label.place(x=150, y=540)
        self.e_dep_combo = Combobox(ve, textvariable=self.e_dep_combo, values=("Accounting", "Anatomy", "Animal-husbandry", "Business-Administration", "Bio-chemistry", "Chemistry", "Child-Education", "Civil-Engineering", "Computer-Engineering", "Computer-Science", "Economics", "Electrical-Engineering", "English-And-Literary-Studies", "Finance", "History", "Human-Kinetics", "Industrial-Chemistry", "International-Relations-And-Project-Management", "Law", "Linguistics", "Mass-Communication", "Mathematics", "Mechanical-Engineering", "Medicine-And-Surgery", "Microbiology", "Physics", "Physiology", "Plant-Science", "Soil-Science", "Theatre-And-Media-Arts", "Vocational-Education"), font=("Calibri", 13, "bold"), width=19)
        self.e_dep_combo.place(x=310, y=540)
        self.e_des_label = Label(ve, text="DESIGNATION:", font=("Calibri", 13, "bold"), bg="white", fg="black")
        self.e_des_label.place(x=150, y=600)
        self.e_des_combo = Combobox(ve, textvariable=self.e_des_combo, values=("Vice-Chansellor", "Dean", "Sub-Dean", "Head-of-Department", "Senior-Lecturer", "Junior-Lecturer"), font=("Calibri", 13, "bold"), width=19)
        self.e_des_combo.place(x=310, y=600)
        self.e_save_btn = Button(ve, text="Save", font=("Arial", 20, "bold"), bg="orangered", fg="black", activebackground="orangered", relief="flat", command=self.save_employee)
        self.e_save_btn.place(x=250, y=650)

    # generate an employee ID
    def random_employee_id(self):
        self.letters = string.ascii_letters.upper()
        self.random_letters = [random.choice(self.letters) for i in range(2)]
        self.ran = ''.join(self.random_letters)
        self.number_list = []
        k = 1
        while k <= 4:
            self.number = random.randint(0, 9)
            self.number_list.append(self.number)
            k += 1
        s = [str(i) for i in self.number_list]
        self.res = (''.join(s))
        self.val = self.res + self.ran
        print("EMPLOYEE ID:", self.val)
        return self.val

    # define a function to save student information
    def save_employee(self):
        self.eid = self.ei_entry.get().upper()
        self.efn = self.efn_entry.get().upper()
        self.eln = self.eln_entry.get().upper()
        try:
            self.ea = str(self.ea_entry.get())
        except:
            messagebox.showwarning("Error", "Enter age in digits")
        self.eg = self.e_gender1.get().upper()
        try:
            self.esc = self.e_sal_entry.get()
        except:
            messagebox.showwarning("Error", "Enter salary in digits")
        self.edp = self.e_dep_combo.get().upper()
        self.edg = self.e_des_combo.get().upper()
        self.date = time.ctime()

        # condition for processing
        if self.eid == self.value4 and self.ea and self.esc and self.edp and self.edg:
            conn = sqlite3.connect("Learn_More_University.db")

            try:
                cursor = conn.cursor()

                insert_employee_query = "INSERT INTO Employee (employeeID, first_name, last_name, age, gender, salary, department, designation) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

                cursor.execute(insert_employee_query, (self.eid, self.efn, self.eln, self.ea, self.eg, self.esc, self.edp, self.edg))
                conn.commit()
                messagebox.showinfo("Success", "Info added successfully")
                ve.destroy()

            except sqlite3.Error as e:
                messagebox.showerror("Error", "Info not successfully added")
                print("SQLite error:", e)
                conn.rollback()

            finally:
                conn.close()
                from learn_more_uni import main_lmu_app

        else:
            messagebox.showwarning("Error", "Invalid Employee ID")

    # function to close student form and entry
    def close_employee(self):
        ve.destroy()


emp_form = EF(ve)
emp_form.mainloop()
