from tkinter import *


def close_splash_screen():
    splash_screen.destroy()
    main_cal_app()


def main_cal_app():
    window = Tk()
    window.title("Wizard Calculator")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = 327
    window_height = 510
    x_axis = (screen_width - window_width) // 2
    y_axis = (screen_height - window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{x_axis}+{y_axis}")
    window.configure(bg="gray10")
    image = PhotoImage(file="cala1.png")
    window.iconphoto(False, image)

    class Calculator(Frame):
        def __init__(self, master):
            super().__init__(master)
            self.grid()
            self.create_widgets()

        def clearbox(self):
            self.display_answer.delete(0, END)

        def create_widgets(self):

            self.number = StringVar()

            self.display_answer = Entry(window, textvariable=self.number, justify="right", font=("Arial", 20, "bold"),
                                        width=21, fg="white", bg="gray10", borderwidth=0)
            self.display_answer.place(x=2, y=70)
            self.mc = Button(window, text="MC", font=("Arial", 9, "bold"), bg="gray10", fg="white", height=1, width=7,
                             borderwidth=0, state='disabled')
            self.mc.place(x=3, y=150)
            self.mr = Button(window, text="MR", font=("Arial", 9, "bold"), bg="gray10", fg="white", height=1, width=7,
                             borderwidth=0, state='disabled')
            self.mr.place(x=57, y=150)
            self.mplus = Button(window, text="M+", font=("Arial", 9, "bold"), bg="gray10", fg="white", height=1,
                                width=7, borderwidth=0)
            self.mplus.place(x=111, y=150)
            self.mminus = Button(window, text="M-", font=("Arial", 9, "bold"), bg="gray10", fg="white", height=1,
                                 width=7, borderwidth=0)
            self.mminus.place(x=165, y=150)
            self.ms = Button(window, text="MS", font=("Arial", 9, "bold"), bg="gray10", fg="white", height=1, width=7,
                             borderwidth=0)
            self.ms.place(x=219, y=150)
            self.mdown = Button(window, text="M<>", font=("Arial", 9, "bold"), bg="gray10", fg="white", height=1,
                                width=7, borderwidth=0, state='disabled')
            self.mdown.place(x=273, y=150)
            self.percent = Button(window, text="%", font=("Arial", 8, "bold"), bg="gray14", fg="white", height=3,
                                  width=10, borderwidth=0, command=lambda text="%": self.entry_displayed(text))
            self.percent.place(x=3, y=177)
            self.lnx = Button(window, text="1/x", font=("Arial", 8, "bold"), bg="gray14", fg="white", height=3,
                              width=10, borderwidth=0, command=lambda text="1/x": self.divisible_x())
            self.lnx.place(x=3, y=232)
            self.seven = Button(window, text="7", font=("Arial", 8, "bold"), bg="gray14", fg="white", height=3,
                                width=10, borderwidth=0, command=lambda text="7": self.entry_displayed(text))
            self.seven.place(x=3, y=287)
            self.four = Button(window, text="4", font=("Arial", 8, "bold"), bg="gray14", fg="white", height=3, width=10,
                               borderwidth=0, command=lambda text="4": self.entry_displayed(text))
            self.four.place(x=3, y=342)
            self.one = Button(window, text="1", font=("Arial", 8, "bold"), bg="gray14", fg="white", height=3, width=10,
                              borderwidth=0, command=lambda text="1": self.entry_displayed(text))
            self.one.place(x=3, y=397)
            self.plus_divide_minus = Button(window, text="+/-", font=("Arial", 8, "bold"), bg="gray14", fg="white",
                                            height=3, width=8, borderwidth=0,
                                            command=lambda text="+/-": self.negate_value())
            self.plus_divide_minus.place(x=3, y=452)
            self.ce = Button(window, text="CE", font=("Arial", 8, "bold"), bg="gray14", fg="white", height=3, width=10,
                             borderwidth=0, command=self.clearbox)
            self.ce.place(x=85, y=177)
            self.pow2 = Button(window, text="x^2", font=("Arial", 8, "bold"), bg="gray14", fg="white", height=3,
                               width=10, borderwidth=0, command=lambda text="x^2": self.square_x())
            self.pow2.place(x=85, y=232)
            self.eight = Button(window, text="8", font=("Arial", 8, "bold"), bg="gray14", fg="white", height=3,
                                width=10, borderwidth=0, command=lambda text="8": self.entry_displayed(text))
            self.eight.place(x=85, y=287)
            self.five = Button(window, text="5", font=("Arial", 8, "bold"), bg="gray14", fg="white", height=3, width=10,
                               borderwidth=0, command=lambda text="5": self.entry_displayed(text))
            self.five.place(x=85, y=342)
            self.two = Button(window, text="2", font=("Arial", 8, "bold"), bg="gray14", fg="white", height=3, width=10,
                              borderwidth=0, command=lambda text="2": self.entry_displayed(text))
            self.two.place(x=85, y=397)
            self.zero = Button(window, text="0", font=("Arial", 8, "bold"), bg="gray14", fg="white", height=3, width=8,
                               borderwidth=0, command=lambda text="0": self.entry_displayed(text))
            self.zero.place(x=73, y=452)
            self.c = Button(window, text="C", font=("Arial", 8, "bold"), bg="gray14", fg="white", height=3, width=10,
                            borderwidth=0)
            self.c.place(x=167, y=177)
            self.tanx = Button(window, text="sqrt", font=("Arial", 8, "bold"), bg="gray14", fg="white", height=3,
                               width=10, borderwidth=0, command=lambda text="sqrt": self.squareroot_x())
            self.tanx.place(x=167, y=232)
            self.nine = Button(window, text="9", font=("Arial", 8, "bold"), bg="gray14", fg="white", height=3, width=10,
                               borderwidth=0, command=lambda text="9": self.entry_displayed(text))
            self.nine.place(x=167, y=287)
            self.six = Button(window, text="6", font=("Arial", 8, "bold"), bg="gray14", fg="white", height=3, width=10,
                              borderwidth=0, command=lambda text="6": self.entry_displayed(text))
            self.six.place(x=167, y=342)
            self.three = Button(window, text="3", font=("Arial", 8, "bold"), bg="gray14", fg="white", height=3,
                                width=10, borderwidth=0, command=lambda text="3": self.entry_displayed(text))
            self.three.place(x=167, y=397)
            self.dot = Button(window, text=".", font=("Arial", 8, "bold"), bg="gray14", fg="white", height=3, width=8,
                              borderwidth=0, command=lambda text=".": self.entry_displayed(text))
            self.dot.place(x=143, y=452)
            self.delt = Button(window, text="<|", font=("Arial", 8, "bold"), bg="gray14", fg="white", height=3,
                               width=10, borderwidth=0, command=lambda text="<|": self.clear_one())
            self.delt.place(x=249, y=177)
            self.divide = Button(window, text="/", font=("Arial", 8, "bold"), bg="gray14", fg="white", height=3,
                                 width=10, borderwidth=0, command=lambda text="/": self.entry_displayed(text))
            self.divide.place(x=249, y=232)
            self.times = Button(window, text="X", font=("Arial", 8, "bold"), bg="gray14", fg="white", height=3,
                                width=10, borderwidth=0, command=lambda text="*": self.entry_displayed(text))
            self.times.place(x=249, y=287)
            self.minus = Button(window, text="-", font=("Arial", 8, "bold"), bg="gray14", fg="white", height=3,
                                width=10, borderwidth=0, command=lambda text="-": self.entry_displayed(text))
            self.minus.place(x=249, y=342)
            self.plus = Button(window, text="+", font=("Arial", 8, "bold"), bg="gray14", fg="white", height=3, width=10,
                               borderwidth=0, command=lambda text="+": self.entry_displayed(text))
            self.plus.place(x=249, y=397)
            self.equal = Button(window, text="=", font=("Arial", 8, "bold"), bg="red", fg="white", height=3, width=15,
                                borderwidth=0, command=lambda text="=": self.entry_displayed(text))
            self.equal.place(x=213, y=452)

        def entry_displayed(self, char):
            if char == "=":
                try:
                    self.value = eval(self.number.get())
                    self.number.set(self.value)
                except:
                    self.number.set("Err...")
            else:
                self.display_char = self.number.get()
                self.new_char = self.display_char + char
                self.number.set(self.new_char)

        def clear_one(self):
            self.val = self.number.get()
            if self.val:
                self.new_val = self.val[:-1]
                self.display_answer.delete(0, END)
                self.display_answer.insert(0, self.new_val)

        def negate_value(self):
            self.val = self.number.get()
            if self.val:
                self.new_val = "-" + self.val
                self.display_answer.delete(0, END)
                self.display_answer.insert(0, self.new_val)

        def divisible_x(self):
            self.val = self.number.get()
            if self.val:
                self.new_val = 1 / float(self.val)
                self.number.set(str(self.new_val))

        def square_x(self):
            self.val = self.number.get()
            if self.val:
                self.new_val = float(self.val) ** 2
                self.number.set(str(self.new_val))

        def squareroot_x(self):
            self.val = self.number.get()
            if self.val:
                self.new_val = float(self.val) ** 0.5
                self.number.set(str(self.new_val))

    calculator_app = Calculator(window)
    calculator_app.mainloop()


splash_screen = Tk()
splash_screen.overrideredirect(True)

scr_width = splash_screen.winfo_screenwidth()
scr_height = splash_screen.winfo_screenheight()
splash_width = 308
splash_height = 307
x_coordinate = (scr_width - splash_width) // 2
y_coordinate = (scr_height - splash_height) // 2
splash_screen.geometry(f"{splash_width}x{splash_height}+{x_coordinate}+{y_coordinate}")
splash_screen.configure(background="gray10")

img = PhotoImage(file="cala1.png")

img_label = Label(splash_screen, image=img, width=310, height=305)
img_label.place(y=1)

splash_screen.after(1000, close_splash_screen)
splash_screen.mainloop()
