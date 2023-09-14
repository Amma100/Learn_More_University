def student_form(self):
    # create an instance for the entry form for the user
    self.ue = Tk()
    self.ue.config(bg="gray10")
    self.ue.overrideredirect(True)
    msg_wid = 600
    msg_hig = 720
    scrn_wid = self.ue.winfo_screenwidth()
    scrn_hig = self.ue.winfo_screenheight()
    x_axis = (scrn_wid - msg_wid) // 2
    y_axis = (scrn_hig - msg_hig) // 2
    self.ue.geometry(f"{msg_wid}x{msg_hig}+{x_axis}+{y_axis}")

    self.id_entry = StringVar()
    self.fn_entry = StringVar()
    self.ln_entry = StringVar()
    self.age_entry = IntVar()
    self.gender = StringVar()
    self.combo_course = StringVar()

    # get the value that the user selects
    self.sd_label = Label(self.ue, text="STUDENT ID:", font=("Calibri", 13, "bold"), bg="white", fg="black")
    self.sd_label.place(x=210, y=180)
    # condition statement for further processing
    self.value1 = self.random_student_id()
    self.sd = Label(self.ue, text="STUDENT ENTRY", font=("Calibri", 30, "bold", "italic"), bg="white", fg="black")
    self.sd.place(x=170, y=100)
    self.sd_label.config(text=f"STUDENT ID: {self.value1}")
    self.esi_label = Label(self.ue, text="STUDENT ID:", font=("Calibri", 13, "bold"), bg="white", fg="black")
    self.esi_label.place(x=150, y=240)
    self.esi_entry = Entry(self.ue, textvariable=self.id_entry, font=("Calibri", 13))
    self.esi_entry.place(x=280, y=240)
    self.efn_label = Label(self.ue, text="FIRST NAME:", font=("Calibri", 13, "bold"), bg="white", fg="black")
    self.efn_label.place(x=150, y=300)
    self.efn_entry = Entry(self.ue, textvariable=self.fn_entry, font=("Calibri", 13))
    self.efn_entry.place(x=280, y=300)
    self.eln_label = Label(self.ue, text="LAST NAME:", font=("Calibri", 13, "bold"), bg="white", fg="black")
    self.eln_label.place(x=150, y=360)
    self.eln_entry = Entry(self.ue, textvariable=self.ln_entry, font=("Calibri", 13))
    self.eln_entry.place(x=280, y=360)
    self.ea_label = Label(self.ue, text="AGE:", font=("Calibri", 13, "bold"), bg="white", fg="black")
    self.ea_label.place(x=150, y=420)
    self.ea_entry = Entry(self.ue, textvariable=self.age_entry, font=("Calibri", 13))
    self.ea_entry.place(x=280, y=420)
    self.gender_label = Label(self.ue, text="GENDER:", font=("Calibri", 13, "bold"), bg="white", fg="black")
    self.gender_label.place(x=150, y=480)
    self.male_btn = Radiobutton(self.ue, text="Male", variable=self.gender, font=("Calibri", 13), value="Male",
                                activebackground="black", relief="flat")
    self.male_btn.place(x=280, y=480)
    self.female_btn = Radiobutton(self.ue, text="Female", variable=self.gender, font=("Calibri", 13), value="Female",
                                  activebackground="black", relief="flat")
    self.female_btn.place(x=380, y=480)
    self.course_label = Label(self.ue, text="COURSE ENROLLED:", font=("Calibri", 13, "bold"), bg="white", fg="black")
    self.course_label.place(x=150, y=540)
    self.course_combo = Combobox(self.ue, textvariable=self.combo_course, values=(
        "Accounting", "Anatomy", "Animal husbandry", "Business Administration", "Bio-chemistry", "Chemistry",
        "Child  Education", "Civil Engineering", "Computer Engineering", "Computer Science", "Economics",
        "Electrical Engineering", "English And Literary Studies", "Finance", "History", "Human Kinetics",
        "Industrial Chemistry", "International Relations And Project Management", "Law", "Linguistics",
        "Mass Communication", "Mathematics", "Mechanical Engineering", "Medicine And Surgery", "Microbiology",
        "Physics",
        "Physiology", "Plant Science", "Soil Science", "Theatre And Media Arts", "Vocational Education"),
                                 font=("Calibri", 13, "bold"), width=19)
    self.course_combo.place(x=310, y=540)
    self.save_btn = Button(self.ue, text="Save", font=("Arial", 21, "bold"), bg="orangered", fg="black",
                           activebackground="orangered", relief="flat")
    self.save_btn.place(x=250, y=600)
    self.close_btn = Button(self.ue, text="X", font=("Arial", 13, "bold"), bg="red", fg="black", activebackground="red",
                            width=3, relief="flat", command=self.close_student)
    self.close_btn.place(x=563)

    self.ue.mainloop()
