from tkinter import *


class Calculator(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # app header created

        Label(Calc_window, text="Amarachi Calculator", font=("Arial", 17, "bold"), bg="gray10", fg="white").place(
            x=112.5, y=27)
        # create number display label
        self.first_num = Label(Calc_window, text="1st NUMBER", font=("Arial", 13), bg="gray10", fg="white").place(
            x=80.5, y=115)
        self.second_num = Label(Calc_window, text="2nd NUMBER", font=("Arial", 13), bg="gray10", fg="white").place(
            x=80.5, y=182)
        # create number display entry
        self.first_num_entry = Entry(Calc_window, width=10, font=("Arial", 13), state="disabled").place(x=274.5, y=115)
        self.second_num_entry = Entry(Calc_window, width=10, font=("Arial", 13)).place(x=274.5, y=182)
        # create arithmetic display buttons
        self.sum_button = Button(Calc_window, text="+", bg="green", fg="white", height=1, width=3,
                                 font=("Arial", 13)).place(x=182.5, y=244)
        self.minus_button = Button(Calc_window, text="-", bg="orangered", fg="white", height=1, width=3,
                                   font=("Arial", 13)).place(x=232.5, y=244)
        self.sum_button = Button(Calc_window, text="x", bg="purple", fg="white", height=1, width=3,
                                 font=("Arial", 13)).place(x=282.5, y=244)
        self.sum_button = Button(Calc_window, text="/", bg="black", fg="white", height=1, width=3,
                                 font=("Arial", 13)).place(x=332.5, y=244)
        self.sum_button = Button(Calc_window, text="=", bg="white", fg="black", height=1, width=7,
                                 font=("Arial", 13)).place(x=232.5, y=295)

        # create a result text display
        self.answer = Label(Calc_window, text="ANSWER", width=10, font=("Arial", 13), bg="gray10", fg="white").place(
            x=80.5, y=350)
        self.answer = Entry(Calc_window, width=15, font=("Arial", 13)).place(x=232.5, y=350)


Calc_window = Tk()
Calc_window.title("Math Wizard - Calculator form")
Calc_window.geometry("450x432")
Calc_window.configure(bg="gray10")
Calc_window = Calculator(Calc_window)
Calc_window.mainloop()
