from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import time


# display a splash screen before LMU app runs
def close_splash_screen():
    splash_screen.destroy()
    main_lmu_app()


# display the main app after splash screen
def main_lmu_app():
    window = Tk()
    window.title("Learn More University Form")
    win_wid = 1300
    win_hig = 820
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = (screen_width - win_wid) // 2
    y_coordinate = (screen_height - win_hig) // 2
    window.geometry(f"{win_wid}x{win_hig}+{x_coordinate}+{y_coordinate}")
    window.config(bg="white")
    image = PhotoImage(file="lmu_logo.png")
    window.iconphoto(False, image)
    img1 = Image.open("b4.png")
    img1 = img1.resize((win_wid, win_hig))
    photo = ImageTk.PhotoImage(img1)
    win_label = Label(window, image=photo)
    win_label.pack(fill="both")

    class LMU(Frame):
        def __init__(self, master):
            super().__init__(master)
            self.lmu_display()
            self.create_ui_widgets()

        # define a display background
        def lmu_display(self):
            self.dis_label = Label(window, width=170, height=13, bg="gray10")
            self.dis_label.place(x=50)

        def create_ui_widgets(self):

            self.combo_user = StringVar()

            # create a menu bar
            self.menu_bar = Menu(window)

            # configure the menu bar to the top of the window
            window.config(menu=self.menu_bar)

            # add file menu to the menu bar
            self.file_menu = Menu(self.menu_bar, tearoff=0)
            self.file_menu.add_command(label="Add student file", command=self.student)
            self.file_menu.add_command(label="Add employee file", command=self.employee)
            self.file_menu.add_separator()
            self.file_menu.add_command(label="View file", command=self.detail)
            self.file_menu.add_separator()
            self.file_menu.add_command(label="Time and Date", command=self.showdt)
            self.file_menu.add_separator()
            self.file_menu.add_command(label="Exit", command=self.exit)

            # add an edit menu bar to the menu bar
            self.edit_menu = Menu(self.menu_bar, tearoff=0)
            self.edit_menu.add_command(label="Update Student File")
            self.edit_menu.add_command(label="Update Employee File")
            self.edit_menu.add_command(label="Delete Student File")
            self.edit_menu.add_command(label="Delete Employee File")

            # add a format menu bar to the menu bar
            self.format_menu = Menu(self.menu_bar, tearoff=0)
            self.format_menu.add_command(label="Bold   ")
            self.format_menu.add_command(label="Italic")

            # add a help menu bar to the menu bar
            self.help_menu = Menu(self.menu_bar, tearoff=0)
            self.help_menu.add_command(label="About")

            # cascade all the menu bars in the menu bar
            self.menu_bar.add_cascade(label="File", menu=self.file_menu)
            self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
            self.menu_bar.add_cascade(label="Format", menu=self.format_menu)
            self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

            # display information in the display background
            self.name_label = Label(window, text="LEARN MORE UNIVERSITY", font=("Calibri", 30, "bold"), bg="gray10", fg="white")
            self.name_label.place(x=400)
            self.contact_label = Label(window, text="CONTACT", font=("Calibri", 13), bg="gray10", fg="white")
            self.contact_label.place(x=70, y=70)
            self.address_label = Label(window, text="Address: 101101 Gregg Jemmer Estate, Trinity road, Lagos Island, Lagos State.", font=("Calibri", 13), bg="gray10", fg="white")
            self.address_label.place(x=70, y=100)
            self.tel_label = Label(window, text="Tel no: +2347087086005, +2349060004598, +2348075050006", font=("Calibri", 13), bg="gray10", fg="white")
            self.tel_label.place(x=70, y=130)
            self.email_label = Label(window, text="Email address: learnmoreuni@gmail.com", font=("Calibri", 13), bg="gray10", fg="white")
            self.email_label.place(x=70, y=160)

            # create a welcome background
            self.welcome_label = Label(window, text="WELCOME", font=("Calibri", 25, "bold"), bg="white", fg="black")
            self.welcome_label.place(x=560, y=240)

            # create a combobox for user to select an option
            self.currency_label = Label(window, text="LMU form", font=("Calibri", 15, "bold", "italic"), bg="white", fg="gray11")
            self.currency_label.place(x=420, y=320)
            self.currency_info = Button(window, text="!", font=("Calibri", 10, "bold"), width=2, height=1,  borderwidth=0, bg="orangered", fg="white", relief="flat")
            self.currency_info.place(x=517, y=325)
            self.user_combo = Combobox(window, textvariable=self.combo_user, values=("Add student details", "Add employee details"), font=("Calibri", 15, "bold"), width=44)
            self.user_combo.place(x=420, y=360)
            self.user_combo.bind("<<ComboboxSelected>>", self.entry)  # bind the combobox to an event

        # display an entry form when a combobox is selected
        def entry(self, event):

            # get the value that the user selects
            self.user_value = self.user_combo.get()

            # condition statement for further processing
            if self.user_value == "Add student details":
                window.destroy()
                from student_form import SF

            # condition statement for further processing
            if self.user_value == "Add employee details":
                window.destroy()
                from employee_form import EF

        # display an entry form to save student information
        def student(self):
            window.destroy()
            from student_form import SF

        # display an entry form to save employee information
        def employee(self):
            window.destroy()
            from employee_form import EF

        # display a detail form
        def detail(self):
            window.destroy()
            from lmu_details import DET

        # display date and time
        def showdt(self):
            self.dt = time.ctime()
            messagebox.showinfo("Date and Time", self.dt)

        # exit LMU app
        def exit(self):
            window.destroy()

    lmu_app = LMU(window)
    lmu_app.mainloop()


# create an instance of Tk
splash_screen = Tk()

# override window widgets
splash_screen.overrideredirect(True)

# set splash screen width and heihgt
s_scr_wid = 400
s_scr_hig = 300

# open an image using the PIL module
image = Image.open("lmu_logo.png")
image = image.resize((s_scr_wid, s_scr_hig))
photo = ImageTk.PhotoImage(image)

# get the screen width and height of the system
screen_wid = splash_screen.winfo_screenwidth()
screen_hig = splash_screen.winfo_screenheight()
x_coordinate = (screen_wid - s_scr_wid) // 2
y_coordinate = (screen_hig - s_scr_hig) // 2

# calculate the splash screen geometry and center it
splash_screen.geometry(f"{s_scr_wid}x{s_scr_hig}+{x_coordinate}+{y_coordinate}")

# create a label to view the image and fit it to the splash screen
image_label = Label(splash_screen, image=photo)
image_label.pack()

# close the splash screen after 2 sec
splash_screen.after(2, close_splash_screen)
splash_screen.mainloop()
