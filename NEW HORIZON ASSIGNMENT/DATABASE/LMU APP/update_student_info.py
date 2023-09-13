from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from student_up import SUF

us = Tk()
us.config(bg="white")
us.title("Student-Update")

msg_wid = 600
msg_hig = 400
scrn_wid = us.winfo_screenwidth()
scrn_hig = us.winfo_screenheight()
x_axis = (scrn_wid - msg_wid) // 2
y_axis = (scrn_hig - msg_hig) // 2
us.geometry(f"{msg_wid}x{msg_hig}+{x_axis}+{y_axis}")
pic = PhotoImage(file="lmu_logo.png")
us.iconphoto(False, pic)
image = Image.open("b3.jpg")
image = image.resize((msg_wid, msg_hig))
background_image = ImageTk.PhotoImage(image)
us_label = Label(us, image=background_image)
us_label.pack()


class US(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.student_update()

    # display an entry form when an "add student file is clicked" is selected
    def student_update(self):

        self.s_id_entry = StringVar()
        self.s_combo_value = StringVar()

        # get the value that the user selects
        self.sd_label = Label(us, text="STUDENT UPDATE", font=("Calibri", 30, "bold"), bg="black", fg="white")
        self.sd_label.place(x=150, y=20)
        self.stu_id_label = Label(us, text="STUDENT ID:", font=("Calibri", 15, "bold"), bg="black", fg="white")
        self.stu_id_label.place(x=30, y=120)
        self.stu_id_entry = Entry(us, textvariable=self.s_id_entry, font=("Calibri", 15))
        self.stu_id_entry.place(x=190, y=120)
        self.val_combo = Combobox(us, textvariable=self.s_combo_value, values=("FIRST NAME", "LAST NAME", "AGE", "GENDER", "COURSE ENROLLED"), font=("Calibri", 13, "bold"), width=31)
        self.val_combo.place(x=153, y=200)
        self.val_combo.bind("<<ComboboxSelected>>", self.choose_val)
        self.val_label = Label(us, text="", font=("Calibri", 15, "bold"))
        self.val_label.place(x=30, y=260)

    def choose_val(self, event):
        self.get_val = self.val_combo.get()
        self.s_fn_entry = StringVar()
        self.s_ln_entry = StringVar()
        self.s_ag_entry = IntVar()
        self.s_gen = StringVar()
        self.s_cmb_course = StringVar()

        # condition statement for further processing
        if self.get_val == "FIRST NAME":
            self.val_label.config(text="FIRST NAME:", bg="black", fg="white")
            self.s_fname_entry = Entry(us, textvariable=self.s_fn_entry, font=("Calibri", 13))
            self.s_fname_entry.place(x=190, y=260)
            self.s_savefn_btn = Button(us, text="Save", font=("Arial", 21, "bold"), bg="orangered", fg="black", activebackground="orangered", relief="flat", command=self.fname_update)
            self.s_savefn_btn.place(x=250, y=330)
            self.s_lname_entry.destroy()
            self.s_age_entry.destroy()
            self.s_m_gender.destroy()
            self.s_f_gender.destroy()
            self.s_course_combo.destroy()
            self.s_saveln_btn.destroy()
            self.s_saveag_btn.destroy()
            self.s_savegen_btn.destroy()
            self.s_savec_btn.destroy()

        elif self.get_val == "LAST NAME":
            self.val_label.config(text="LAST NAME:", bg="black", fg="white")
            self.s_lname_entry = Entry(us, textvariable=self.s_ln_entry, font=("Calibri", 13))
            self.s_lname_entry.place(x=185, y=260)
            self.s_saveln_btn = Button(us, text="Save", font=("Arial", 21, "bold"), bg="orangered", fg="black", activebackground="orangered", relief="flat", command=self.lname_update)
            self.s_saveln_btn.place(x=250, y=330)
            self.s_fname_entry.destroy()
            self.s_age_entry.destroy()
            self.s_m_gender.destroy()
            self.s_f_gender.destroy()
            self.s_course_combo.destroy()
            self.s_savefn_btn.destroy()
            self.s_saveag_btn.destroy()
            self.s_savegen_btn.destroy()
            self.s_savec_btn.destroy()

        elif self.get_val == "AGE":
            self.val_label.config(text="AGE:", bg="black", fg="white")
            self.s_age_entry = Entry(us, textvariable=self.s_ag_entry, font=("Calibri", 13), width=10)
            self.s_age_entry.place(x=110, y=260)
            self.s_age_entry.delete(0, END)
            self.s_saveag_btn = Button(us, text="Save", font=("Arial", 21, "bold"), bg="orangered", fg="black", activebackground="orangered", relief="flat", command=self.age)
            self.s_saveag_btn.place(x=250, y=330)
            self.s_fname_entry.destroy()
            self.s_lname_entry.destroy()
            self.s_m_gender.destroy()
            self.s_f_gender.destroy()
            self.s_course_combo.destroy()
            self.s_savefn_btn.destroy()
            self.s_saveln_btn.destroy()
            self.s_savegen_btn.destroy()
            self.s_savec_btn.destroy()

        elif self.get_val == "GENDER":
            self.val_label.config(text="GENDER:", bg="black", fg="white")
            self.s_m_gender = Radiobutton(us, variable=self.s_gen, text="Male", value="Male", font=("Calibri", 13, "bold"))
            self.s_m_gender.place(x=180, y=260)
            self.s_m_gender.select()
            self.s_f_gender = Radiobutton(us, variable=self.s_gen, text="Female", value="Female", font=("Calibri", 13, "bold"))
            self.s_f_gender.place(x=280, y=260)
            self.s_savegen_btn = Button(us, text="Save", font=("Arial", 21, "bold"), bg="orangered", fg="black", activebackground="orangered", relief="flat", command=self.gender)
            self.s_savegen_btn.place(x=250, y=330)
            self.s_fname_entry.destroy()
            self.s_lname_entry.destroy()
            self.s_age_entry.destroy()
            self.s_course_combo.destroy()
            self.s_savefn_btn.destroy()
            self.s_saveln_btn.destroy()
            self.s_saveag_btn.destroy()
            self.s_savec_btn.destroy()

        elif self.get_val == "COURSE ENROLLED":
            self.val_label.config(text="COURSE ENROLLED:", bg="black", fg="white")
            self.s_course_combo = Combobox(us, textvariable=self.s_cmb_course, values=("Accounting", "Anatomy", "Animal-husbandry", "Business-Administration", "Bio-chemistry", "Chemistry", "Child-Education", "Civil-Engineering", "Computer-Engineering", "Computer-Science", "Economics", "Electrical-Engineering", "English-And-Literary-Studies", "Finance", "History", "Human-Kinetics", "Industrial-Chemistry", "International-Relations-And-Project-Management", "Law", "Linguistics", "Mass-Communication", "Mathematics", "Mechanical-Engineering", "Medicine-And-Surgery", "Microbiology", "Physics", "Physiology", "Plant-Science", "Soil-Science", "Theatre-And-Media-Arts", "Vocational-Education"), font=("Calibri", 13, "bold"), width=19)
            self.s_course_combo.place(x=250, y=260)
            self.s_savec_btn = Button(us, text="Save", font=("Arial", 21, "bold"), bg="orangered", fg="black", activebackground="orangered", relief="flat", command=self.course)
            self.s_savec_btn.place(x=250, y=330)
            self.s_fname_entry.destroy()
            self.s_lname_entry.destroy()
            self.s_age_entry.destroy()
            self.s_m_gender.destroy()
            self.s_f_gender.destroy()
            self.s_savefn_btn.destroy()
            self.s_saveln_btn.destroy()
            self.s_saveag_btn.destroy()
            self.s_savegen_btn.destroy()

    def fname_update(self):
        self.val_id = self.stu_id_entry.get()
        self.val_fname = self.s_fname_entry.get().upper()
        SUF.first_name(self.val_id, self.val_fname)
        messagebox.showinfo("Update Successful", "First name updated to {} successfully".format(self.val_fname))

    def lname_update(self):
        self.val2_id = self.stu_id_entry.get()
        self.val2_lname = self.s_lname_entry.get().upper()
        SUF.last_name(self.val2_id, self.val2_lname)
        messagebox.showinfo("Update Successful", "Last name updated to {} successfully".format(self.val2_lname))

    def age(self):
        self.val3_id = self.stu_id_entry.get()
        self.val3_age = self.s_age_entry.get()
        SUF.age(self.val3_id, self.val3_age)
        messagebox.showinfo("Update Successful", "Age updated to {} successfully".format(self.val3_age))

    def gender(self):
        self.val4_id = self.stu_id_entry.get()
        self.val4_gender = self.s_gen.get()
        SUF.gender(self.val4_id, self.val4_gender)
        messagebox.showinfo("Update Successful", "Gender updated to {} successfully".format(self.val4_gender))

    def course(self):
        self.val5_id = self.stu_id_entry.get()
        self.val5_course = self.s_course_combo.get()
        SUF.course(self.val5_id, self.val5_course)
        messagebox.showinfo("Update Successful", "Course updated to {} successfully".format(self.val5_course))


su_app = US(us)
su_app.mainloop()
