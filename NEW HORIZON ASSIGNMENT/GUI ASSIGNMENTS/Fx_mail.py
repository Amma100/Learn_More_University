from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import re
import time


def close_splash_screen():
    splash_screen.destroy()
    main_mail_app()


def main_mail_app():
    mail_window = Tk()
    mail_window.title("FX Mail V1.0")
    scr_width = mail_window.winfo_screenwidth()
    scr_height = mail_window.winfo_screenheight()
    mail_width = 650
    mail_height = 535
    x_coordinate = (scr_width - mail_width) // 2
    y_coordinate = (scr_height - mail_height) // 2
    mail_window.geometry(f"{mail_width}x{mail_height}+{x_coordinate}+{y_coordinate}")
    image1 = PhotoImage(file="maill.png")
    mail_window.iconphoto(False, image1)
    back_image = Image.open("blacki.jpg")
    back_image = back_image.resize((mail_width, mail_height))
    back_photo = ImageTk.PhotoImage(back_image)
    back_label = Label(mail_window, image=back_photo)
    back_label.pack()

    class Fx_mail(Frame):
        def __init__(self, master):
            super().__init__(master)
            self.mail_widget()

        def mail_widget(self):

            self.frm = StringVar()
            self.sub = StringVar()
            self.To = StringVar()

            self.from_label = Label(mail_window, text="From:", font=("Arial", 10, "bold", "italic"), bg="gray1", fg="white")
            self.from_label.place(x=30, y=39)
            self.from_entry = Entry(mail_window, textvariable=self.frm, width=28, font=("Arial", 10))
            self.from_entry.place(x=92, y=39)
            self.Subject_label = Label(mail_window, text="Subject:", font=("Arial", 10, "bold", "italic"), bg="gray1", fg="white")
            self.Subject_label.place(x=30, y=80)
            self.Subject_entry = Entry(mail_window, textvariable=self.sub, width=28, font=("Arial", 10))
            self.Subject_entry.place(x=92, y=80)
            self.To_label = Label(mail_window, text="To:", font=("Arial", 10, "bold", "italic"), bg="gray1", fg="white")
            self.To_label.place(x=30, y=119)
            self.To_entry = Entry(mail_window, textvariable=self.To, width=28, font=("Arial", 10))
            self.To_entry.place(x=92, y=119)
            self.idk2_btn = Button(mail_window, width=3, font=("Arial", 10, "bold"), bg="gray11", fg="white")
            self.idk2_btn.place(x=318, y=113)
            self.idk_btn = Button(mail_window, text="...", font=("Arial", 10, "bold"), width=3, bg="black", fg="white")
            self.idk_btn.place(x=315, y=110)
            self.Compose_text = Text(mail_window,  width=86, height=15, font=("Arial", 10), bg="gray95")
            self.Compose_text.place(x=20, y=179)
            self.quit_btn = Button(mail_window, font=("Arial", 10, "bold"), width=5, bg="gray11", fg="white")
            self.quit_btn.place(x=478, y=440)
            self.quit_btn = Button(mail_window, text="Quit", font=("Arial", 10, "bold"), width=5, bg="black", fg="white", command=lambda text="Quit": self.qt_btn())
            self.quit_btn.place(x=475, y=437)
            self.send_btn = Button(mail_window, font=("Arial", 10, "bold"), width=5, bg="gray11", fg="white")
            self.send_btn.place(x=568, y=440)
            self.send_btn = Button(mail_window, text="Send", font=("Arial", 10, "bold"), width=5, bg="black", fg="white", command=lambda text="Send": self.snd_btn())
            self.send_btn.place(x=565, y=437)
            self.ready_label = Label(mail_window, text="Ready", font=("Arial", 10, "bold", "italic"), bg="gray1", fg="white")
            self.ready_label.place(x=20, y=490)

        def qt_btn(self):
            self.value_1 = self.from_entry.get()
            self.value_2 = self.Subject_entry.get()
            self.value_3 = self.To_entry.get()
            self.value_4 = self.Compose_text.get("1.0", "end-1c")
            if (self.value_1 != "") and (self.value_3 != "") and (self.value_4 != ""):
                messagebox.showinfo("Info", "Your mail will be saved as a draft")
                self.from_entry.delete(0, END)
                self.Subject_entry.delete(0, END)
                self.To_entry.delete(0, END)
                self.Compose_text.delete("1.0", "end-1c")
            elif (self.value_1 == "") and (self.value_3 == "") and (self.value_4 == ""):
                messagebox.showinfo("Info", "Your message box is already empty")
            elif (self.value_1 == "") and (self.value_3 == "") and (self.value_4 != ""):
                self.Compose_text.delete(0, END)
            elif (self.value_1 == "") or (self.value_3 == "") and (self.value_4 != ""):
                self.from_entry.delete(0, END)
                self.Subject_entry.delete(0, END)
                self.To_entry.delete(0, END)
                self.Compose_text.delete(0, END)
            elif (self.value_1 == "") or (self.value_3 == "") and (self.value_4 == ""):
                self.from_entry.delete(0, END)
                self.Subject_entry.delete(0, END)
                self.To_entry.delete(0, END)
                self.Compose_text.delete(0, END)
            elif (self.value_1 != "") and (self.value_3 != "") and (self.value_4 == ""):
                self.from_entry.delete(0, END)
                self.Subject_entry.delete(0, END)
                self.To_entry.delete(0, END)
                self.Compose_text.delete(0, END)

        def snd_btn(self):
            self.value_1 = self.from_entry.get()
            self.value_2 = self.Subject_entry.get()
            self.value_3 = self.To_entry.get()
            self.value_4 = self.Compose_text.get("1.0", "end-1c")
            self.tm = time.ctime()
            self.frm = re.match("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Z,a-z]{2,3}", self.value_1)
            print(self.frm)
            self.to = re.match("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Z,a-z]{2,3}", self.value_3)
            print(self.to)

            if self.frm and self.to and (self.value_4 != ""):
                messagebox.showinfo("Success", "Mail Sent successfully")
                print("Mail sent successfully at {}".format(self.tm))
            elif self.frm and self.to and (self.value_4 == ""):
                messagebox.showinfo("Error", "Message box is empty")
            elif self.frm and self.to is None and (self.value_4 != ""):
                messagebox.showinfo("Failure", "Mail not Sent\nInvalid receiver email address")
            elif self.frm and self.to is None and (self.value_4 == ""):
                messagebox.showinfo("Failure", "Mail not Sent\nInvalid receiver email address")
            elif self.frm is None and self.to and (self.value_4 != ""):
                messagebox.showinfo("Failure", "Mail not Sent\nInvalid sender email address")
            elif self.frm is None and self.to and (self.value_4 == ""):
                messagebox.showinfo("Failure", "Mail not Sent\nInvalid sender email address")
            elif self.frm is None and self.to is None and (self.value_4 != ""):
                messagebox.showinfo("Failure", "Mail not Sent\nInvalid sender and receiver email addresses")
            elif self.frm is None and self.to is None and (self.value_4 == ""):
                messagebox.showinfo("Failure", "Mail not Sent\nInvalid sender and receiver email addresses")

    mail_app = Fx_mail(mail_window)
    mail_app.mainloop()


splash_screen = Tk()
splash_screen.overrideredirect(True)

img = Image.open("maill3.png")
splash_width = 400
splash_height = 300
img = img.resize((splash_width, splash_height))
photo = ImageTk.PhotoImage(img)
screen_width = splash_screen.winfo_screenwidth()
screen_height = splash_screen.winfo_screenheight()
x_axs = (screen_width - splash_width) // 2
y_axs = (screen_height - splash_height) // 2
splash_screen.geometry(f"{splash_width}x{splash_height}+{x_axs}+{y_axs}")
splash_screen.configure(background="gray10")


img_label = Label(splash_screen, image=photo)
img_label.pack()


splash_screen.after(2000, close_splash_screen)
splash_screen.mainloop()
