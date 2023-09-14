import random
import re
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk


def close_splash_screen():
    splash_screen.destroy()
    lottery_app()


def lottery_app():
    lottery_window = Tk()
    lottery_window.title("Wazza Lottery")
    lottery_window_width = 600
    lottery_window_height = 800
    scr_width = lottery_window.winfo_screenwidth()
    scr_height = lottery_window.winfo_screenheight()
    x_axis = (scr_width - lottery_window_width) // 2
    y_axis = (scr_height - lottery_window_height) // 2
    lottery_window.geometry(f"{lottery_window_width}x{lottery_window_height}+{x_axis}+{y_axis}")
    image = PhotoImage(file="choose-lottery-numbers.png")
    lottery_window.iconphoto(False, image)
    bg_image = Image.open("casino1.jpg")
    bg_image = bg_image.resize((lottery_window_width, lottery_window_height))
    bg_render = ImageTk.PhotoImage(bg_image)
    bg_label = Label(lottery_window, image=bg_render)
    bg_label.pack()

    class Wazza_lottery_app(Frame):
        def __init__(self, master):
            super().__init__(master)
            self.create_order_request_widget()

        def create_circle(self, canvas, x, y, radius, **kwargs):
            return canvas.create_oval(x - radius, y - radius, x + radius, y + radius, **kwargs)

        def create_order_request_widget(self):

            self.f_num = IntVar()
            self.s_num = IntVar()
            self.balance = IntVar()

            self.wazza_name_label = Label(lottery_window, text="WAZZA LOTTERY", font=("Arial", 30, "bold"), bg="cyan1",
                                          fg="black")
            self.wazza_name_label.place(x=130, y=30)

            # create a canvas and display a number in a circle form
            self.background_image = Image.open("casino1.jpg")
            self.background_photo = ImageTk.PhotoImage(self.background_image)
            self.canvas = Canvas(lottery_window, width=450, height=105, borderwidth=3)
            self.canvas.create_image(0, 0, anchor=NW, image=self.background_photo)
            self.canvas.place(x=75, y=100)
            self.circle_x1 = 100
            self.circle_y1 = 55
            self.circle_rad1 = 50
            self.circle_color1 = "red"
            self.circle_x2 = 360
            self.circle_y2 = 55
            self.circle_rad2 = 50
            self.circle_color2 = "green"
            self.circle1 = self.create_circle(self.canvas, self.circle_x1, self.circle_y1, self.circle_rad1,
                                              fill=self.circle_color1)
            self.circle1 = self.create_circle(self.canvas, self.circle_x2, self.circle_y2, self.circle_rad2,
                                              fill=self.circle_color2)
            self.label1 = Label(self.canvas, text="", bg=self.circle_color1, fg="white", font=("Arial", 30, "bold"))
            self.label1.place(x=self.circle_x1, y=self.circle_y1, anchor="center")
            self.label2 = Label(self.canvas, text="", bg=self.circle_color2, fg="white", font=("Arial", 30, "bold"))
            self.label2.place(x=self.circle_x2, y=self.circle_y2, anchor="center")
            self.first_label = Label(lottery_window, text="Guess first number", font=("Arial", 15, "bold", "italic"),
                                     bg="yellow1", fg="black")
            self.first_label.place(x=205, y=250)
            self.first_entry = Entry(lottery_window, textvariable=self.f_num, font=("Arial", 15, "bold", "italic"),
                                     width=4, justify="center", bg="red", fg="white")
            self.first_entry.place(x=275, y=300)
            self.first_entry.delete(0, END)
            self.second_label = Label(lottery_window, text="Guess second number", font=("Arial", 15, "bold", "italic"),
                                      bg="yellow1", fg="black")
            self.second_label.place(x=195, y=350)
            self.second_entry = Entry(lottery_window, textvariable=self.s_num, font=("Arial", 15, "bold", "italic"),
                                      width=4, justify="center", bg="green", fg="white")
            self.second_entry.place(x=275, y=400)
            self.second_entry.delete(0, END)
            self.multiplier_label = Label(lottery_window, text="Multiplier", font=("Arial", 15, "bold", "italic"),
                                          bg="red4", fg="white")
            self.multiplier_label.place(x=215, y=470)
            self.multiplier_num_label = Label(lottery_window, text="", font=("Arial", 15, "bold", "italic"), bg="red4",
                                              fg="white", width=5)
            self.multiplier_num_label.place(x=335, y=470)
            self.play_btn_dec = Button(lottery_window, text="PLAY", font=("Arial", 25, "bold"), bg="black", fg="black",
                                       borderwidth=2)
            self.play_btn_dec.place(x=241, y=526)
            self.play_btn = Button(lottery_window, text="PLAY", font=("Arial", 25, "bold"), bg="orangered3", fg="black",
                                   activebackground="black", relief="raised", command=self.play_btn)
            self.play_btn.place(x=235, y=520)
            self.how_play_btn_dec = Button(lottery_window, text="How to play", font=("Arial", 10, "bold"), bg="black",
                                           fg="black", borderwidth=2)
            self.how_play_btn_dec.place(x=18, y=666)
            self.how_play_btn = Button(lottery_window, text="How to play", font=("Arial", 10, "bold"), bg="cyan1",
                                       fg="black", activebackground="black", relief="raised", command=self.h_t_p)
            self.how_play_btn.place(x=12, y=660)
            self.balance_label = Label(lottery_window, text="BALANCE", font=("Arial", 25, "bold"), bg="pink3",
                                       fg="black")
            self.balance_label.place(x=12, y=720)
            self.balance_entry = Entry(lottery_window, textvariable=self.balance, font=("Arial", 15, "bold", "italic"),
                                       width=1)
            self.balance_entry.place(x=182, y=720)
            self.balance_entry.delete(0, END)
            self.balance_entry.insert(0, "100000")
            self.balance_label = Label(lottery_window, text="₦100000", font=("Arial", 25, "bold"), bg="white",
                                       fg="black")
            self.balance_label.place(x=182, y=720)

        # generate a number
        def random_num(self):
            self.number_list = []
            k = 1
            while k <= 2:
                self.number = random.randint(0, 9)
                self.number_list.append(self.number)
                if self.number_list[0] == 0:
                    self.number_list.remove(self.number)
                    return self.random_num()
                k += 1
            s = [str(i) for i in self.number_list]
            result = (''.join(s))
            return result

        # run this code when the play button is clicked
        def play_btn(self):
            # get the first number
            self.value1 = self.first_entry.get()
            # using regular expression to validate if first number is a digit
            self.regex_value1 = re.match("\d{1,2}", self.value1)
            print(self.regex_value1)
            # get the second number
            self.value2 = self.second_entry.get()
            # using regular expression to validate if second number is a digit
            self.regex_value2 = re.match("\d{1,2}", self.value2)
            print(self.regex_value2)
            # conditions for play button
            if self.value1 == "" and self.value2 == "":
                messagebox.showinfo("Info", "Enter your guessed numbers to play game")
            elif self.value1 != "" and self.value2 == "":
                messagebox.showinfo("Info", "Guess your second number")
            elif self.value1 == "" and self.value2 != "":
                messagebox.showinfo("Info", "Guess your first number")
            else:
                if self.value1 != "" and self.value2 != "":
                    if self.regex_value1 is None and self.regex_value2 is None:
                        messagebox.showinfo("Error", "Enter a correct numbers\ne.g 12, 83, 98, 30")
                    elif self.regex_value1 and self.regex_value2 is None:
                        messagebox.showinfo("Error", "Enter a valid digit for your second number")
                    elif self.regex_value1 is None and self.regex_value2:
                        messagebox.showinfo("Error", "Enter a valid digit for yor first number")
                    else:
                        if self.regex_value1 and self.regex_value2:
                            # save a random number in guess1
                            self.guess1 = self.random_num()
                            print(self.guess1)
                            # save a random number in guess2
                            self.guess2 = self.random_num()
                            print(self.guess2)
                            # save a random multiplier in multi variable
                            self.multi = self.random_num()
                            self.multiply_label = self.multi + "x"
                            print(self.multiply_label)
                            self.bal = self.balance_entry.get()
                            print(self.bal)
                            if int(self.bal) == 0:
                                messagebox.showinfo("Info",
                                                    "You don't have enough money to play :(\n\nDeposit and try again")
                            elif self.value1 != self.guess1 and self.value2 != self.guess2:
                                self.balance = int(self.bal) - 5000
                                self.balance_entry.delete(0, END)
                                self.balance_entry.insert(0, str(self.balance))
                                self.balance_label.config(text="₦" + str(self.balance))
                                print(self.balance)
                                # configure each label to show a value when the play button is clicked
                                self.multiplier_num_label.config(text=self.multiply_label)
                                self.label1.config(text=self.guess1)
                                self.label2.config(text=self.guess2)
                                self.first_entry.delete(0, END)
                                self.second_entry.delete(0, END)
                                messagebox.showinfo("Info", "You didn't guess any number right :(\n\nTry again")
                            elif self.value1 == self.guess1 and self.value2 == self.guess2:
                                self.balance = int(self.bal) - 5000
                                self.new_balance = (5000 * self.multi) + self.balance
                                self.balance_entry.delete(0, END)
                                self.balance_entry.insert(0, str(self.new_balance))
                                self.balance_label.config(text="₦" + str(self.new_balance))
                                print(self.balance)
                                print(f"5000 x {self.multi} + {self.balance} = {self.new_balance}")
                                # configure each label to show a value when the play button is clicked
                                self.multiplier_num_label.config(text=self.multiply_label)
                                self.label1.config(text=self.guess1)
                                self.label2.config(text=self.guess2)
                                self.first_entry.delete(0, END)
                                self.second_entry.delete(0, END)
                                messagebox.showinfo("Info",
                                                    "LEGEND!!!\nYou guessed all the numbers right :)\n\nTry your luck again")
                            elif self.value1 != self.guess1 and self.value2 == self.guess2:
                                self.balance = int(self.bal) - 5000
                                self.new_balance = (5000 * (int(self.multi // 2))) + self.balance
                                self.balance_entry.delete(0, END)
                                self.balance_entry.insert(0, str(self.new_balance))
                                self.balance_label.config(text="₦" + str(self.new_balance))
                                print(self.balance)
                                print(f"5000 x ({self.multi} // 2) + {self.balance} = {self.new_balance}")
                                # configure each label to show a value when the play button is clicked
                                self.multiplier_num_label.config(text=self.multiply_label)
                                self.label1.config(text=self.guess1)
                                self.label2.config(text=self.guess2)
                                self.first_entry.delete(0, END)
                                self.second_entry.delete(0, END)
                                messagebox.showinfo("Info", "CHAMPION!!!\nYou guessed one number right :)\n\nTry again")
                            elif self.value1 == self.guess1 and self.value2 != self.guess2:
                                self.balance = int(self.balance) - 5000
                                self.new_balance = (5000 * (int(self.multi // 2))) + self.balance
                                self.balance_entry.delete(0, END)
                                self.balance_entry.insert(0, str(self.new_balance))
                                self.balance_label.config(text="₦" + str(self.new_balance))
                                print(self.balance)
                                print(f"5000 x ({self.multi} // 2) + {self.balance} = {self.new_balance}")
                                # configure each label to show a value when the play button is clicked
                                self.multiplier_num_label.config(text=self.multiply_label)
                                self.label1.config(text=self.guess1)
                                self.label2.config(text=self.guess2)
                                self.first_entry.delete(0, END)
                                self.second_entry.delete(0, END)
                                messagebox.showinfo("Info", "CHAMPION!!!\nYou guessed one number right :)\n\nTry again")

        def h_t_p(self):
            messagebox.showinfo("Help",
                                "How to play\n========\n\nStep 1: Guess 2 numbers from 1 - 99 to stand a chance to win amazing prices with max combos.\nGuess a number in the red and green pots and see if it shows in the display screen exactly respectively\nStep 2: If one out of the 2 numbers you guessed is correct, you will get some combos\n\n-Have fun and win big!!!")

    wazza_app = Wazza_lottery_app(lottery_window)
    wazza_app.mainloop()


splash_screen = Tk()
splash_screen.overrideredirect(True)
screen_width = splash_screen.winfo_screenwidth()
screen_height = splash_screen.winfo_screenheight()
splash_width = 300
splash_height = 200
x_coordinate = (screen_width - splash_width) // 2
y_coordinate = (screen_height - splash_height) // 2
splash_screen.geometry(f"{splash_width}x{splash_height}+{x_coordinate}+{y_coordinate}")
img = Image.open("card_casino.jpg")
img = img.resize((splash_width, splash_height))
photo = ImageTk.PhotoImage(img)
photo_label = Label(splash_screen, image=photo)
photo_label.pack()

splash_screen.after(2000, close_splash_screen)
splash_screen.mainloop()
