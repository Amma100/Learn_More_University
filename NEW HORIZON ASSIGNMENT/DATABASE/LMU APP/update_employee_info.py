from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from employee_up import EUF

ue = Tk()
ue.config(bg="white")
ue.title("Student-Update")

msg_wid = 600
msg_hig = 400
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
us_label = Label(ue, image=background_image)
us_label.pack()


class US(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.employee_update()

    # display an entry form when an "add student file is clicked" is selected
    def employee_update(self):

        self.e_id_entry = StringVar()
        self.e_combo_value = StringVar()

        # get the value that the user selects
        self.ed_label = Label(ue, text="EMPLOYEE UPDATE", font=("Calibri", 30, "bold"), bg="black", fg="white")
        self.ed_label.place(x=150, y=20)
        self.e_id_label = Label(ue, text="EMPLOYEE ID:", font=("Calibri", 15, "bold"), bg="black", fg="white")
        self.e_id_label.place(x=30, y=120)
        self.e_id_entry = Entry(ue, textvariable=self.e_id_entry, font=("Calibri", 15))
        self.e_id_entry.place(x=190, y=120)
        self.val_combo = Combobox(ue, textvariable=self.e_combo_value, values=("FIRST NAME", "LAST NAME", "AGE", "GENDER", "SALARY", "DEPARTMENT", "DESIGNATION"), font=("Calibri", 13, "bold"), width=31)
        self.val_combo.place(x=153, y=200)
        self.val_combo.bind("<<ComboboxSelected>>", self.choose_val)
        self.val_label = Label(ue, text="", font=("Calibri", 15, "bold"))
        self.val_label.place(x=30, y=260)

    def choose_val(self, event):
        self.get_val = self.val_combo.get()
        self.e_fn_entry = StringVar()
        self.e_ln_entry = StringVar()
        self.e_ag_entry = IntVar()
        self.e_gen = StringVar()
        self.e_sal = IntVar()
        self.e_depa = StringVar()
        self.e_desi = StringVar()

        # condition statement for further processing
        if self.get_val == "FIRST NAME":
            self.val_label.config(text="FIRST NAME:", bg="black", fg="white")
            self.e_fname_entry = Entry(ue, textvariable=self.e_fn_entry, font=("Calibri", 13))
            self.e_fname_entry.place(x=190, y=260)
            self.e_savefn_btn = Button(ue, text="Save", font=("Arial", 21, "bold"), bg="orangered", fg="black", activebackground="orangered", relief="flat", command=self.fname_update)
            self.e_savefn_btn.place(x=250, y=330)
            self.e_lname_entry.destroy()
            self.e_age_entry.destroy()
            self.e_m_gender.destroy()
            self.e_f_gender.destroy()
            self.e_entry.destroy()
            self.dep_combo.destroy()
            self.des_combo.destroy()
            self.e_saveln_btn.destroy()
            self.e_saveag_btn.destroy()
            self.e_savegen_btn.destroy()
            self.e_saves_btn.destroy()
            self.e_savedep_btn.destroy()
            self.e_savedes_btn.destroy()

        elif self.get_val == "LAST NAME":
            self.val_label.config(text="LAST NAME:", bg="black", fg="white")
            self.e_lname_entry = Entry(ue, textvariable=self.e_ln_entry, font=("Calibri", 13))
            self.e_lname_entry.place(x=185, y=260)
            self.e_saveln_btn = Button(ue, text="Save", font=("Arial", 21, "bold"), bg="orangered", fg="black", activebackground="orangered", relief="flat", command=self.lname_update)
            self.e_saveln_btn.place(x=250, y=330)
            self.e_fname_entry.destroy()
            self.e_age_entry.destroy()
            self.e_m_gender.destroy()
            self.e_f_gender.destroy()
            self.e_entry.destroy()
            self.dep_combo.destroy()
            self.des_combo.destroy()
            self.e_savefn_btn.destroy()
            self.e_saveag_btn.destroy()
            self.e_savegen_btn.destroy()
            self.e_saves_btn.destroy()
            self.e_savedep_btn.destroy()
            self.e_savedes_btn.destroy()

        elif self.get_val == "AGE":
            self.val_label.config(text="AGE:", bg="black", fg="white")
            self.e_age_entry = Entry(ue, textvariable=self.e_ag_entry, font=("Calibri", 13), width=10)
            self.e_age_entry.place(x=110, y=260)
            self.e_age_entry.delete(0, END)
            self.e_saveag_btn = Button(ue, text="Save", font=("Arial", 21, "bold"), bg="orangered", fg="black", activebackground="orangered", relief="flat", command=self.age)
            self.e_saveag_btn.place(x=250, y=330)
            self.e_fname_entry.destroy()
            self.e_lname_entry.destroy()
            self.e_m_gender.destroy()
            self.e_f_gender.destroy()
            self.e_entry.destroy()
            self.dep_combo.destroy()
            self.des_combo.destroy()
            self.e_savefn_btn.destroy()
            self.e_saveln_btn.destroy()
            self.e_savegen_btn.destroy()
            self.e_saves_btn.destroy()
            self.e_savedep_btn.destroy()
            self.e_savedes_btn.destroy()

        elif self.get_val == "GENDER":
            self.val_label.config(text="GENDER:", bg="black", fg="white")
            self.e_m_gender = Radiobutton(ue, variable=self.e_gen, text="Male", value="Male", font=("Calibri", 13, "bold"))
            self.e_m_gender.place(x=180, y=260)
            self.e_m_gender.select()
            self.e_f_gender = Radiobutton(ue, variable=self.e_gen, text="Female", value="Female", font=("Calibri", 13, "bold"))
            self.e_f_gender.place(x=280, y=260)
            self.e_savegen_btn = Button(ue, text="Save", font=("Arial", 21, "bold"), bg="orangered", fg="black", activebackground="orangered", relief="flat", command=self.gender)
            self.e_savegen_btn.place(x=250, y=330)
            self.e_fname_entry.destroy()
            self.e_lname_entry.destroy()
            self.e_age_entry.destroy()
            self.e_entry.destroy()
            self.dep_combo.destroy()
            self.des_combo.destroy()
            self.e_savefn_btn.destroy()
            self.e_saveln_btn.destroy()
            self.e_saveag_btn.destroy()
            self.e_saves_btn.destroy()
            self.e_savedep_btn.destroy()
            self.e_savedes_btn.destroy()

        elif self.get_val == "SALARY":
            self.val_label.config(text="SALARY:", bg="black", fg="white")
            self.e_entry = Entry(ue, textvariable=self.e_sal, font=("Calibri", 13, "bold"))
            self.e_entry.place(x=150, y=260)
            self.e_entry.delete(0, END)
            self.e_saves_btn = Button(ue, text="Save", font=("Arial", 21, "bold"), bg="orangered", fg="black", activebackground="orangered", relief="flat", command=self.salary)
            self.e_saves_btn.place(x=250, y=330)
            self.e_fname_entry.destroy()
            self.e_lname_entry.destroy()
            self.e_age_entry.destroy()
            self.e_m_gender.destroy()
            self.e_f_gender.destroy()
            self.dep_combo.destroy()
            self.des_combo.destroy()
            self.e_savefn_btn.destroy()
            self.e_saveln_btn.destroy()
            self.e_saveag_btn.destroy()
            self.e_savegen_btn.destroy()
            self.e_savedep_btn.destroy()
            self.e_savedes_btn.destroy()

        elif self.get_val == "DEPARTMENT":
            self.val_label.config(text="DEPARTMENT:", bg="black", fg="white")
            self.dep_combo = Combobox(ue, textvariable=self.e_depa, font=("Calibri", 13, "bold"), values=("Accounting", "Anatomy", "Animal-husbandry", "Business-Administration", "Bio-chemistry", "Chemistry", "Child-Education", "Civil-Engineering", "Computer-Engineering", "Computer-Science", "Economics", "Electrical-Engineering", "English-And-Literary-Studies", "Finance", "History", "Human-Kinetics", "Industrial-Chemistry", "International-Relations-And-Project-Management", "Law", "Linguistics", "Mass-Communication", "Mathematics", "Mechanical-Engineering", "Medicine-And-Surgery", "Microbiology", "Physics", "Physiology", "Plant-Science", "Soil-Science", "Theatre-And-Media-Arts", "Vocational-Education"), width=19)
            self.dep_combo.place(x=190, y=260)
            self.e_savedep_btn = Button(ue, text="Save", font=("Arial", 21, "bold"), bg="orangered", fg="black", activebackground="orangered", relief="flat", command=self.dept)
            self.e_savedep_btn.place(x=250, y=330)
            self.e_fname_entry.destroy()
            self.e_lname_entry.destroy()
            self.e_age_entry.destroy()
            self.e_m_gender.destroy()
            self.e_f_gender.destroy()
            self.e_entry.destroy()
            self.des_combo.destroy()
            self.e_savefn_btn.destroy()
            self.e_saveln_btn.destroy()
            self.e_saveag_btn.destroy()
            self.e_savegen_btn.destroy()
            self.e_saves_btn.destroy()
            self.e_savedes_btn.destroy()

        elif self.get_val == "DESIGNATION":
            self.val_label.config(text="DEPARTMENT:", bg="black", fg="white")
            self.des_combo = Combobox(ue, textvariable=self.e_desi, font=("Calibri", 13, "bold"), values=("Vice-Chansellor", "Dean", "Sub-Dean", "Head-of-Department", "Senior-Lecturer", "Junior-Lecturer"), width=19)
            self.des_combo.place(x=190, y=260)
            self.e_savedes_btn = Button(ue, text="Save", font=("Arial", 21, "bold"), bg="orangered", fg="black", activebackground="orangered", relief="flat", command=self.desig)
            self.e_savedes_btn.place(x=250, y=330)
            self.e_fname_entry.destroy()
            self.e_lname_entry.destroy()
            self.e_age_entry.destroy()
            self.e_m_gender.destroy()
            self.e_f_gender.destroy()
            self.e_entry.destroy()
            self.dep_combo.destroy()
            self.e_savefn_btn.destroy()
            self.e_saveln_btn.destroy()
            self.e_saveag_btn.destroy()
            self.e_savegen_btn.destroy()
            self.e_saves_btn.destroy()
            self.e_savedep_btn.destroy()

    def fname_update(self):
        self.val_id = self.e_id_entry.get()
        self.val_fname = self.e_fname_entry.get().upper()
        EUF.first_name(self.val_id, self.val_fname)
        messagebox.showinfo("Update Successful", "First name updated to {} successfully".format(self.val_fname))

    def lname_update(self):
        self.val2_id = self.e_id_entry.get()
        self.val2_lname = self.e_lname_entry.get().upper()
        EUF.last_name(self.val2_id, self.val2_lname)
        messagebox.showinfo("Update Successful", "Last name updated to {} successfully".format(self.val2_lname))

    def age(self):
        self.val3_id = self.e_id_entry.get()
        self.val3_age = self.e_age_entry.get()
        EUF.age(self.val3_id, self.val3_age)
        messagebox.showinfo("Update Successful", "Age updated to {} successfully".format(self.val3_age))

    def gender(self):
        self.val4_id = self.e_id_entry.get()
        self.val4_gender = self.e_gen.get()
        EUF.gender(self.val4_id, self.val4_gender)
        messagebox.showinfo("Update Successful", "Gender updated to {} successfully".format(self.val4_gender))

    def salary(self):
        self.val5_id = self.e_id_entry.get()
        self.val5_course = self.e_entry.get()
        EUF.salary(self.val5_id, self.val5_course)
        messagebox.showinfo("Update Successful", "Course updated to {} successfully".format(self.val5_course))

    def dept(self):
        self.val6_id = self.e_id_entry.get()
        self.val6_course = self.dep_combo.get()
        EUF.department(self.val6_id, self.val6_course)
        messagebox.showinfo("Update Successful", "Course updated to {} successfully".format(self.val6_course))

    def desig(self):
        self.val7_id = self.e_id_entry.get()
        self.val7_course = self.des_combo.get()
        EUF.designation(self.val7_id, self.val7_course)
        messagebox.showinfo("Update Successful", "Course updated to {} successfully".format(self.val7_course))


su_app = US(ue)
su_app.mainloop()
