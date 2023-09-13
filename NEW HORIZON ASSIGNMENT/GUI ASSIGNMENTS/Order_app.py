import re
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from PIL import Image, ImageTk


def close_splash_screen():
    splash_screen.destroy()
    main_order_app()


def main_order_app():
    order_window = Tk()
    order_window.title("Order Request")
    order_window_width = 600
    order_window_height = 640
    scr_width = order_window.winfo_screenwidth()
    scr_height = order_window.winfo_screenheight()
    x_axis = (scr_width - order_window_width) // 2
    y_axis = (scr_height - order_window_height) // 2
    order_window.geometry(f"{order_window_width}x{order_window_height}+{x_axis}+{y_axis}")
    image = PhotoImage(file="cock4.png")
    order_window.iconphoto(False, image)
    bg_image = Image.open("cock1.jpg")
    bg_image = bg_image.resize((order_window_width, order_window_height))
    bg_render = ImageTk.PhotoImage(bg_image)
    bg_label = Label(order_window, image=bg_render)
    bg_label.pack()

    class Order_request_app(Frame):
        def __init__(self, master):
            super().__init__(master)
            self.create_order_request_widget()

        def create_order_request_widget(self):

            self.fl_name = StringVar()
            self.email = StringVar()
            self.phone = StringVar()
            self.phone_combo = StringVar()
            self.loc = StringVar()
            self.check1 = IntVar()
            self.check2 = IntVar()
            self.check3 = IntVar()
            self.radio = StringVar()

            self.info1_label_des = Label(order_window,
                                         text="PLEASE FILL THE FORM BELOW TO ORDER FOR YOUR ICE CUBES, BARS AND DRINKS",
                                         font=("Arial", 10, "bold"), bg="black", fg="black")
            self.info1_label_des.place(x=27, y=12)
            self.info1_label = Label(order_window,
                                     text="PLEASE FILL THE FORM BELOW TO ORDER FOR YOUR ICE CUBES, BARS AND DRINKS",
                                     font=("Arial", 10, "bold"), bg="darkorchid4", fg="white")
            self.info1_label.place(x=19, y=5)
            self.info2_label_des = Label(order_window, text="Fields marked with * are mandatory",
                                         font=("Arial", 10, "bold"), bg="black", fg="black")
            self.info2_label_des.place(x=27, y=62)
            self.info2_label = Label(order_window, text="Fields marked with * are mandatory",
                                     font=("Arial", 10, "bold"), bg="darkorchid4", fg="white")
            self.info2_label.place(x=19, y=55)
            self.full_name_label_des = Label(order_window, text="Full Name *", font=("Arial", 10, "bold"), bg="black",
                                             fg="black")
            self.full_name_label_des.place(x=54, y=116)
            self.full_name_label = Label(order_window, text="Full Name *", font=("Arial", 10, "bold"), bg="deeppink3",
                                         fg="white")
            self.full_name_label.place(x=46, y=109)
            self.full_name_entry = Entry(order_window, textvariable=self.fl_name, font=("Arial", 10, "bold"), width=30)
            self.full_name_entry.place(x=46, y=143)
            self.email_label_des = Label(order_window, text="Email *", font=("Arial", 10, "bold"), bg="black",
                                         fg="black")
            self.email_label_des.place(x=326, y=116)
            self.email_label = Label(order_window, text="Email *", font=("Arial", 10, "bold"), bg="deeppink3",
                                     fg="white")
            self.email_label.place(x=318, y=109)
            self.email_entry = Entry(order_window, textvariable=self.email, font=("Arial", 10, "bold"), width=30)
            self.email_entry.place(x=318, y=143)
            self.phone_label_des = Label(order_window, text="Phone Number *", font=("Arial", 10, "bold"), bg="black",
                                         fg="black")
            self.phone_label_des.place(x=54, y=203)
            self.phone_label = Label(order_window, text="Phone Number *", font=("Arial", 10, "bold"), bg="deeppink3",
                                     fg="white")
            self.phone_label.place(x=46, y=196)
            self.combo_phone = Combobox(order_window, textvariable=self.phone_combo, values=("+1", "+234"),
                                        font=("Arial", 10, "bold"), width=4, background="black", foreground="white")
            self.combo_phone.place(x=170, y=199)
            self.phone_entry = Entry(order_window, textvariable=self.phone, font=("Arial", 10, "bold"), width=30)
            self.phone_entry.place(x=46, y=230)
            self.location_label_des = Label(order_window, text="Location", font=("Arial", 10, "bold"), bg="black",
                                            fg="black")
            self.location_label_des.place(x=326, y=203)
            self.location_label = Label(order_window, text="Location", font=("Arial", 10, "bold"), bg="deeppink3",
                                        fg="white")
            self.location_label.place(x=318, y=196)
            self.location_entry = Entry(order_window, textvariable=self.loc, font=("Arial", 10, "bold"), width=30)
            self.location_entry.place(x=318, y=230)
            self.delivery_label_des = Label(order_window, text="Delivery Address", font=("Arial", 10, "bold"),
                                            bg="black", fg="black")
            self.delivery_label_des.place(x=54, y=297)
            self.delivery_label = Label(order_window, text="Delivery Address", font=("Arial", 10, "bold"),
                                        bg="deeppink3", fg="white")
            self.delivery_label.place(x=46, y=290)
            self.delivery_entry = Text(order_window, font=("Arial", 10, "bold"), width=30, height=10)
            self.delivery_entry.place(x=46, y=324)
            self.order_label_des = Label(order_window, text="Order Type *", font=("Arial", 10, "bold"), bg="black",
                                         fg="black")
            self.order_label_des.place(x=326, y=297)
            self.order_label = Label(order_window, text="Order Type *", font=("Arial", 10, "bold"), bg="deeppink3",
                                     fg="white")
            self.order_label.place(x=318, y=290)
            self.chk1 = Checkbutton(order_window, variable=self.check1, text="Ice cubes", font=("Arial", 10, "bold"),
                                    activebackground="black", relief="raised")
            self.chk1.place(x=318, y=337)
            self.chk2 = Checkbutton(order_window, variable=self.check2, text="Ice bars", font=("Arial", 10, "bold"),
                                    activebackground="black", relief="raised")
            self.chk2.place(x=318, y=377)
            self.chk3 = Checkbutton(order_window, variable=self.check3, text="Drinks services",
                                    font=("Arial", 10, "bold"), activebackground="black", relief="raised")
            self.chk3.place(x=318, y=417)
            self.qa_label = Label(order_window, text="Require mobile bar?", font=("Arial", 10, "bold"), bg="black",
                                  fg="black")
            self.qa_label.place(x=27, y=511)
            self.qa_label = Label(order_window, text="Require mobile bar?", font=("Arial", 10, "bold"),
                                  bg="darkorchid4", fg="white")
            self.qa_label.place(x=19, y=504)
            self.yes_radio = Radiobutton(order_window, variable=self.radio, text="Yes", font=("Arial", 10, "bold"),
                                         value="Yes", activebackground="black", relief="raised")
            self.yes_radio.place(x=179, y=504)
            self.no_radio = Radiobutton(order_window, variable=self.radio, text="No", font=("Arial", 10, "bold"),
                                        value="No", activebackground="black", relief="raised")
            self.no_radio.place(x=239, y=504)
            self.no_radio.select()
            self.snd_odr_btn = Button(order_window, text="Send Order", font=("Arial", 10, "bold"), bg="black",
                                      fg="black")
            self.snd_odr_btn.place(x=260, y=586)
            self.snd_odr_btn = Button(order_window, text="Send Order", font=("Arial", 10, "bold"), bg="orangered",
                                      fg="black", command=self.send_order)
            self.snd_odr_btn.place(x=254, y=580)
            self.combo_phone.bind("<<ComboboxSelected>>", self.ph_val)
            self.phone_entry.bind("<<FocusOut>>", self.send_order)

        def ph_val(self, event):
            self.combo = self.combo_phone.get()
            if self.combo == "+1":
                self.val = "+1-"
                self.phone_entry.delete(0, END)
                self.phone_entry.insert(0, self.val)
            elif self.combo == "+234":
                self.val = "+234-"
                self.phone_entry.delete(0, END)
                self.phone_entry.insert(0, self.val)

        def send_order(self):
            self.value1 = self.full_name_entry.get()
            print(self.value1)
            self.value2 = self.email_entry.get()
            print(self.value2)
            self.value3 = self.phone_entry.get()
            print(self.value3)
            self.value4 = self.location_entry.get()
            print(self.value4)
            self.value5 = self.delivery_entry.get("1.0", "end-1c")
            print(self.value5)
            self.value6 = self.check1.get()
            print(self.value6)
            self.value7 = self.check2.get()
            print(self.value7)
            self.value8 = self.check3.get()
            print(self.value8)
            self.value9 = self.radio.get()
            print(self.value9)
            self.frm_email = re.match("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Z,a-z]{2,3}", self.value2)
            print(self.frm_email)
            self.frm_phone = re.match("[+\w]{1,3}[-\w]{10}", self.value3)
            print(self.frm_phone)
            if self.value1 and self.frm_email and self.frm_phone:
                if self.value6 == 0 and self.value7 == 0 and self.value8 == 0:
                    messagebox.showinfo("Info", "No order selected")
                if self.value6 == 0 and self.value7 == 0 and self.value8 == 1:
                    messagebox.showinfo("Info", "Your order for Drinks services is on its way")

                if self.value6 == 0 and self.value7 == 1 and self.value8 == 0:
                    messagebox.showinfo("Info", "Your order for Ice bars is on its way")
                if self.value6 == 0 and self.value7 == 1 and self.value8 == 1:
                    messagebox.showinfo("Info", "Your order for Ice bars and Drinks services are on its way")
                if self.value6 == 1 and self.value7 == 0 and self.value8 == 0:
                    messagebox.showinfo("Info", "Your order for Ice cubes is on its way")
                if self.value6 == 1 and self.value7 == 0 and self.value8 == 1:
                    messagebox.showinfo("Info", "Your order for Ice cubes and Drinks services are on its way")
                if self.value6 == 1 and self.value7 == 1 and self.value8 == 0:
                    messagebox.showinfo("Info", "Your order for Ice cubes and Ice bars are on its way")
                if self.value6 == 1 and self.value7 == 1 and self.value8 == 1:
                    messagebox.showinfo("Info", "Your order for Ice cubes, Ice bars and Drinks services is on its way")
            elif self.value1 == "" and self.value2 == "" and self.value3 == "":
                messagebox.showinfo("Error", "Please fill all the mandatory information")
            elif self.value1 == "" and self.value2 == "" and self.value3 != "":
                messagebox.showinfo("Error", "Please fill all the mandatory information")
            elif self.value1 == "" and self.value2 != "" and self.value3 == "":
                messagebox.showinfo("Error", "Please fill all the mandatory information")
            elif self.value1 == "" and self.value2 != "" and self.value3 != "":
                messagebox.showinfo("Error", "Please fill in your full name")
            elif self.value1 != "" and self.value2 == "" and self.value3 == "":
                messagebox.showinfo("Error", "Please fill all the mandatory information")
            elif self.value1 != "" and self.value2 == "" and self.value3 != "":
                messagebox.showinfo("Error", "Please fill in your email address")
            elif self.value1 != "" and self.frm_email is None and self.value3 != "":
                messagebox.showinfo("Error", "Invalid email address\nPlease fill in a correct email address")
            elif self.value1 != "" and self.value2 != "" and self.value3 == "":
                messagebox.showinfo("Error", "Please fill in your phone number")
            elif self.value1 != "" and self.value2 != "" and self.frm_phone is None:
                messagebox.showinfo("Error",
                                    "Invalid phone number\nPlease enter a valid 10 digit phone number\ne.g 1234567890")

    order_app = Order_request_app(order_window)
    order_app.mainloop()


splash_screen = Tk()
splash_screen.overrideredirect(True)
screen_width = splash_screen.winfo_screenwidth()
screen_height = splash_screen.winfo_screenheight()
splash_width = 300
splash_height = 200
x_coordinate = (screen_width - splash_width) // 2
y_coordinate = (screen_height - splash_height) // 2
splash_screen.geometry(f"{splash_width}x{splash_height}+{x_coordinate}+{y_coordinate}")
img = Image.open("cock3.jpg")
img = img.resize((splash_width, splash_height))
photo = ImageTk.PhotoImage(img)
photo_label = Label(splash_screen, image=photo)
photo_label.pack()

splash_screen.after(2000, close_splash_screen)
splash_screen.mainloop()
