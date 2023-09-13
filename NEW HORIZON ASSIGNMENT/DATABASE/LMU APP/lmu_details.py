from tkinter import *
from tkinter.ttk import Combobox
from PIL import Image, ImageTk


# create an instance for the entry form for the user
de = Tk()
de.config(bg="white")
de.title("Search-Details")
msg_wid = 300
msg_hig = 200
scrn_wid = de.winfo_screenwidth()
scrn_hig = de.winfo_screenheight()
x_axis = (scrn_wid - msg_wid) // 2
y_axis = (scrn_hig - msg_hig) // 2
de.geometry(f"{msg_wid}x{msg_hig}+{x_axis}+{y_axis}")
pic = PhotoImage(file="lmu_logo.png")
de.iconphoto(False, pic)
image = Image.open("b3.jpg")
image = image.resize((msg_wid, msg_hig))
background_image = ImageTk.PhotoImage(image)
stu_label = Label(de, image=background_image)
stu_label.pack()


class DET(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.details()

    # display an entry form when an "add employee file is clicked" is selected
    def details(self):

        # add some display widgets
        self.value_combo = StringVar()

        self.detail = Label(de, text="DETAILS", font=("Calibri", 23, "bold"), bg="white", fg="black")
        self.detail.place(x=97, y=55)
        self.view = Combobox(de, textvariable=self.value_combo, values=("VIEW STUDENT DATA", "VIEW EMPLOYEE DATA"), font=("Calibri", 13, "bold"), width=19)
        self.view.place(x=55, y=115)
        self.view.bind("<<ComboboxSelected>>", self.combo_details)

    # define a function to display the combobox
    def combo_details(self, event):
        # create an instance for the entry form for the user
        self.combo = Tk()
        self.combo.config(bg="white")
        self.combo.title("View-Details")
        msg_wid = 250
        msg_hig = 250
        scrn_wid = self.combo.winfo_screenwidth()
        scrn_hig = self.combo.winfo_screenheight()
        x_axis = (scrn_wid - msg_wid) // 2
        y_axis = (scrn_hig - msg_hig) // 2
        self.combo.geometry(f"{msg_wid}x{msg_hig}+{x_axis}+{y_axis}")

        # get the value of the combobox selected
        self.val_combo = StringVar()

        self.de_value = self.view.get()
        # condition statement
        if self.de_value == "VIEW STUDENT DATA":
            de.destroy()
            self.view_by = Label(self.combo, text="VIEW BY", font=("Calibri", 23, "bold"), bg="white", fg="black")
            self.view_by.place(x=67, y=65)
            self.one_student_id = Combobox(self.combo, values=("VIEW DATA BY STUDENT ID", "VIEW ALL STUDENTS DATA"), textvariable=self.val_combo, font=("Calibri", 12), width=19)
            self.one_student_id.place(x=37, y=120)
            self.eclose_btn = Button(self.combo, text="NEXT", font=("Arial", 15, "bold"), bg="orangered", fg="black", activebackground="orangered", relief="flat", command=self.student_next)
            self.eclose_btn.place(x=97, y=190)

        if self.de_value == "VIEW EMPLOYEE DATA":
            de.destroy()
            self.view_by = Label(self.combo, text="VIEW BY", font=("Calibri", 23, "bold"), bg="white", fg="black")
            self.view_by.place(x=67, y=65)
            self.one_employee_id = Combobox(self.combo, textvariable=self.val_combo, font=("Calibri", 12), values=("VIEW DATA BY EMPLOYEE ID", "VIEW ALL EMPLOYEES DATA"), width=19)
            self.one_employee_id.place(x=37, y=120)
            self.eclose_btn = Button(self.combo, text="NEXT", font=("Arial", 15, "bold"), bg="orangered", fg="black", activebackground="orangered", relief="flat", command=self.employee_next)
            self.eclose_btn.place(x=97, y=190)

        self.combo.mainloop()

    # get student info
    def student_next(self):
        self.student_value = self.one_student_id.get()
        self.combo.destroy()

        # condition statement
        if self.student_value == "VIEW DATA BY STUDENT ID":
            from one_student_next_window import OSN

        # condition statement
        if self.student_value == "VIEW ALL STUDENTS DATA":
            from all_student_next_window import AS

    # get employee info
    def employee_next(self):
        self.employee_value = self.one_employee_id.get()
        self.combo.destroy()

        # condition statement
        if self.employee_value == "VIEW DATA BY EMPLOYEE ID":
            from one_employee_next_window import OEN

        # condition statement
        if self.employee_value == "VIEW ALL EMPLOYEES DATA":
            from all_employee_next_window import AE

    # function to close student form and entry
    def close_detail(self):
        de.destroy()


de_app = DET(de)
de_app.mainloop()
