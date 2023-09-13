from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from PIL import Image, ImageTk


def close_splash_screen():
    splash_screen.destroy()
    main_exchange_app()


def main_exchange_app():
    calc_window = Tk()
    calc_window.title("Exchange Rate Calculator")
    scr_wid = calc_window.winfo_screenwidth()
    scr_hig = calc_window.winfo_screenheight()
    cal_wid = 480
    cal_hig = 710
    x_cord = (scr_wid - cal_wid) // 2
    y_cord = (scr_hig - cal_hig) // 2
    calc_window.geometry(f"{cal_wid}x{cal_hig}+{x_cord}+{y_cord}")
    calc_window.configure(bg="gray1")
    image1 = PhotoImage(file="forex.png")
    calc_window.iconphoto(False, image1)
    back_image = Image.open("blacki.jpg")
    back_image = back_image.resize((cal_wid, cal_hig))
    back_photo = ImageTk.PhotoImage(back_image)
    back_label = Label(calc_window, image=back_photo)
    back_label.pack()

    class Exchange_calculator(Frame):
        def __init__(self, master):
            super().__init__(master)
            self.create_calc_widget()

        def create_calc_widget(self):

            self.currency_combo = StringVar()
            self.trade_combo = StringVar()
            self.dollar_num = DoubleVar()
            self.amount_num = DoubleVar()
            self.naira_num = DoubleVar()

            self.exchange_app_label = Label(calc_window, text="EXCHANGE CALCULATOR", font=("Arial", 20, "bold"),
                                            bg="gray11", fg="white")
            self.exchange_app_label.place(x=59, y=19)
            self.currency_label = Label(calc_window, text="CURRENCY", font=("Arial", 12, "bold", "italic"), bg="gray11",
                                        fg="orangered2")
            self.currency_label.place(x=59, y=100)
            self.currency_info = Button(calc_window, text="!", font=("Arial", 8, "bold"), width=2, height=1,
                                        command=self.currency_info, borderwidth=0, bg="gray70", fg="black")
            self.currency_info.place(x=167, y=100)
            self.combo_currency = Combobox(calc_window, textvariable=self.currency_combo, values=(
            "PERFECT MONEY", "BIT COIN", "ETHEREUM", "SOLANA", "DOGE COIN", "POUND", "EURO", "YEN", "FRANC", "RAND",
            "RUBLE", "CEDI"), font=("Arial", 10, "bold"), width=44)
            self.combo_currency.place(x=59, y=141)
            self.trade_label = Label(calc_window, text="BUY OR SELL", font=("Arial", 12, "bold", "italic"), bg="gray11",
                                     fg="orangered2")
            self.trade_label.place(x=59, y=190)
            self.trade_info = Button(calc_window, text="!", font=("Arial", 8, "bold"), width=2, height=1,
                                     command=self.b_s_info, borderwidth=0, bg="gray70", fg="black")
            self.trade_info.place(x=177, y=190)
            self.combo_trade = Combobox(calc_window, textvariable=self.trade_combo, values=("BUY", "SELL"),
                                        font=("Arial", 10, "bold"))
            self.combo_trade.place(x=59, y=230)
            self.dollar_label = Label(calc_window, text="($) DOLLAR", font=("Arial", 12, "bold", "italic"), bg="gray11",
                                      fg="orangered2")
            self.dollar_label.place(x=59, y=279)
            self.trade_info = Button(calc_window, text="!", font=("Arial", 8, "bold"), width=2, height=1,
                                     command=self.dollar_info, borderwidth=0, bg="gray70", fg="black")
            self.trade_info.place(x=165, y=279)
            self.dollar_entry = Entry(calc_window, textvariable=self.dollar_num, font=("Arial", 12, "bold", "italic"))
            self.dollar_entry.place(x=59, y=320)
            self.amount_label = Label(calc_window, text="AMOUNT", font=("Arial", 12, "bold", "italic"), bg="gray11",
                                      fg="orangered2")
            self.amount_label.place(x=59, y=361)
            self.trade_info = Button(calc_window, text="!", font=("Arial", 8, "bold"), width=2, height=1,
                                     command=self.amount_info, borderwidth=0, bg="gray70", fg="black")
            self.trade_info.place(x=145, y=361)
            self.amount_entry = Entry(calc_window, textvariable=self.amount_num, font=("Arial", 12, "bold", "italic"))
            self.amount_entry.place(x=59, y=402)
            self.naira_entry = Entry(calc_window, textvariable=self.naira_num, font=("Arial", 38, "bold", "italic",),
                                     justify="center", width=11, bg="gray91", fg="black")
            self.naira_entry.place(x=91, y=473)
            self.trade_info = Button(calc_window, text="RESET", font=("Arial", 10, "bold", "italic"), width=10,
                                     height=2, command=self.reset_button, bg="gray1", fg="orangered2", borderwidth=8)
            self.trade_info.place(x=190, y=605)
            self.combo_currency.bind("<<ComboboxSelected>>", self.dolar_entry)
            self.combo_trade.bind("<<ComboboxSelected>>", self.dolar_entry)
            self.dollar_entry.bind("<FocusOut>", self.get_naira_amount)
            self.amount_entry.bind("<FocusOut>", self.get_naira_amount)

        def dolar_entry(self, event):
            self.currency_value = self.combo_currency.get()
            self.trade_value = self.combo_trade.get()
            if self.currency_value == "PERFECT MONEY" and self.trade_value == "BUY":
                self.val = 0.00139
                self.dollar_entry.delete(0, END)
                self.dollar_entry.insert(0, str(self.val))
                self.amount_entry.delete(0, END)
            elif self.currency_value == "PERFECT MONEY" and self.trade_value == "SELL":
                self.val = 0.0013
                self.dollar_entry.delete(0, END)
                self.dollar_entry.insert(0, str(self.val))
                self.amount_entry.delete(0, END)
            elif self.currency_value == "BIT COIN" and self.trade_value == "BUY":
                self.val = 26107
                self.dollar_entry.delete(0, END)
                self.dollar_entry.insert(0, str(self.val))
                self.amount_entry.delete(0, END)
            elif self.currency_value == "BIT COIN" and self.trade_value == "SELL":
                self.val = 23679
                self.dollar_entry.delete(0, END)
                self.dollar_entry.insert(0, str(self.val))
                self.amount_entry.delete(0, END)
            elif self.currency_value == "ETHEREUM" and self.trade_value == "BUY":
                self.val = 1668.72
                self.dollar_entry.delete(0, END)
                self.dollar_entry.insert(0, str(self.val))
                self.amount_entry.delete(0, END)
            elif self.currency_value == "ETHEREUM" and self.trade_value == "SELL":
                self.val = 1642.77
                self.dollar_entry.delete(0, END)
                self.dollar_entry.insert(0, str(self.val))
                self.amount_entry.delete(0, END)
            elif self.currency_value == "SOLANA" and self.trade_value == "BUY":
                self.val = 21.78
                self.dollar_entry.delete(0, END)
                self.dollar_entry.insert(0, str(self.val))
                self.amount_entry.delete(0, END)
            elif self.currency_value == "SOLANA" and self.trade_value == "SELL":
                self.val = 19.96
                self.dollar_entry.delete(0, END)
                self.dollar_entry.insert(0, str(self.val))
                self.amount_entry.delete(0, END)
            elif self.currency_value == "DOGE COIN" and self.trade_value == "BUY":
                self.val = 0.062
                self.dollar_entry.delete(0, END)
                self.dollar_entry.insert(0, str(self.val))
                self.amount_entry.delete(0, END)
            elif self.currency_value == "DOGE COIN" and self.trade_value == "SELL":
                self.val = 0.045
                self.dollar_entry.delete(0, END)
                self.dollar_entry.insert(0, str(self.val))
                self.amount_entry.delete(0, END)
            elif self.currency_value == "POUND" and self.trade_value == "BUY":
                self.val = 1.27
                self.dollar_entry.delete(0, END)
                self.dollar_entry.insert(0, str(self.val))
                self.amount_entry.delete(0, END)
            elif self.currency_value == "POUND" and self.trade_value == "SELL":
                self.val = 1.07
                self.dollar_entry.delete(0, END)
                self.dollar_entry.insert(0, str(self.val))
                self.amount_entry.delete(0, END)
            elif self.currency_value == "EURO" and self.trade_value == "BUY":
                self.val = 1.09
                self.dollar_entry.delete(0, END)
                self.dollar_entry.insert(0, str(self.val))
                self.amount_entry.delete(0, END)
            elif self.currency_value == "EURO" and self.trade_value == "SELL":
                self.val = 0.90
                self.dollar_entry.delete(0, END)
                self.dollar_entry.insert(0, str(self.val))
                self.amount_entry.delete(0, END)
            elif self.currency_value == "YEN" and self.trade_value == "BUY":
                self.val = 0.0069
                self.dollar_entry.delete(0, END)
                self.dollar_entry.insert(0, str(self.val))
                self.amount_entry.delete(0, END)
            elif self.currency_value == "YEN" and self.trade_value == "SELL":
                self.val = 0.0058
                self.dollar_entry.delete(0, END)
                self.dollar_entry.insert(0, str(self.val))
                self.amount_entry.delete(0, END)
            elif self.currency_value == "FRANC" and self.trade_value == "BUY":
                self.val = 1.14
                self.dollar_entry.delete(0, END)
                self.dollar_entry.insert(0, str(self.val))
                self.amount_entry.delete(0, END)
            elif self.currency_value == "FRANC" and self.trade_value == "SELL":
                self.val = 0.99
                self.dollar_entry.delete(0, END)
                self.dollar_entry.insert(0, str(self.val))
                self.amount_entry.delete(0, END)
            elif self.currency_value == "RAND" and self.trade_value == "BUY":
                self.val = 0.053
                self.dollar_entry.delete(0, END)
                self.dollar_entry.insert(0, str(self.val))
                self.amount_entry.delete(0, END)
            elif self.currency_value == "RAND" and self.trade_value == "SELL":
                self.val = 0.049
                self.dollar_entry.delete(0, END)
                self.dollar_entry.insert(0, str(self.val))
                self.amount_entry.delete(0, END)
            elif self.currency_value == "RUBLE" and self.trade_value == "BUY":
                self.val = 0.011
                self.dollar_entry.delete(0, END)
                self.dollar_entry.insert(0, str(self.val))
                self.amount_entry.delete(0, END)
            elif self.currency_value == "RUBLE" and self.trade_value == "SELL":
                self.val = 0.009
                self.dollar_entry.delete(0, END)
                self.dollar_entry.insert(0, str(self.val))
                self.amount_entry.delete(0, END)
            elif self.currency_value == "CEDI" and self.trade_value == "BUY":
                self.val = 0.089
                self.dollar_entry.delete(0, END)
                self.dollar_entry.insert(0, str(self.val))
                self.amount_entry.delete(0, END)
            elif self.currency_value == "CEDI" and self.trade_value == "SELL":
                self.val = 0.081
                self.dollar_entry.delete(0, END)
                self.dollar_entry.insert(0, str(self.val))
                self.amount_entry.delete(0, END)

        def get_naira_amount(self, event):
            self.currency_value = self.combo_currency.get()
            self.trade_value = self.combo_trade.get()
            self.dollar_value = self.dollar_entry.get()
            self.amount_value = self.amount_entry.get()
            if len(self.amount_value) == 0:
                self.naira_entry.delete(0, END)
                self.naira_entry.insert(0, self.dollar_value)
            else:
                if self.currency_value == "PERFECT MONEY" and self.trade_value == "BUY":
                    self.naira_amount = float(self.amount_value) / float(self.dollar_value)
                    self.naira_entry.delete(0, END)
                    self.naira_entry.insert(0, "₦" + str(self.naira_amount))
                if self.currency_value == "PERFECT MONEY" and self.trade_value == "SELL":
                    self.dollar_amount = float(self.amount_value) * float(self.dollar_value)
                    self.naira_entry.delete(0, END)
                    self.naira_entry.insert(0, "$" + str(self.dollar_amount))
                if self.currency_value == "BIT COIN" and self.trade_value == "BUY":
                    self.naira_amount = (float(self.amount_value) / float(self.dollar_value)) * 20058864.30
                    self.naira_entry.delete(0, END)
                    self.naira_entry.insert(0, "₦" + str(self.naira_amount))
                if self.currency_value == "BIT COIN" and self.trade_value == "SELL":
                    self.naira_amount = (float(self.amount_value) / float(self.dollar_value)) * 20058864.30
                    self.naira_entry.delete(0, END)
                    self.naira_entry.insert(0, "₦" + str(self.naira_amount))
                if self.currency_value == "ETHEREUM" and self.trade_value == "BUY":
                    self.naira_amount = (float(self.amount_value) / float(self.dollar_value)) * 1282848.84
                    self.naira_entry.delete(0, END)
                    self.naira_entry.insert(0, "₦" + str(self.naira_amount))
                if self.currency_value == "ETHEREUM" and self.trade_value == "SELL":
                    self.naira_amount = (float(self.amount_value) / float(self.dollar_value)) * 1282848.84
                    self.naira_entry.delete(0, END)
                    self.naira_entry.insert(0, "₦" + str(self.naira_amount))
                if self.currency_value == "SOLANA" and self.trade_value == "BUY":
                    self.naira_amount = (float(self.amount_value) / float(self.dollar_value)) * 16469.29
                    self.naira_entry.delete(0, END)
                    self.naira_entry.insert(0, "₦" + str(self.naira_amount))
                if self.currency_value == "SOLANA" and self.trade_value == "SELL":
                    self.naira_amount = (float(self.amount_value) / float(self.dollar_value)) * 16469.29
                    self.naira_entry.delete(0, END)
                    self.naira_entry.insert(0, "₦" + str(self.naira_amount))
                if self.currency_value == "DOGE COIN" and self.trade_value == "BUY":
                    self.naira_amount = (float(self.amount_value) / float(self.dollar_value)) * 49.20
                    self.naira_entry.delete(0, END)
                    self.naira_entry.insert(0, "₦" + str(self.naira_amount))
                if self.currency_value == "DOGE COIN" and self.trade_value == "SELL":
                    self.naira_amount = (float(self.amount_value) / float(self.dollar_value)) * 49.20
                    self.naira_entry.delete(0, END)
                    self.naira_entry.insert(0, "₦" + str(self.naira_amount))
                if self.currency_value == "POUND" and self.trade_value == "BUY":
                    self.naira_amount = (float(self.amount_value) / float(self.dollar_value)) * 976.39
                    self.naira_entry.delete(0, END)
                    self.naira_entry.insert(0, "₦" + str(self.naira_amount))
                if self.currency_value == "POUND" and self.trade_value == "SELL":
                    self.naira_amount = (float(self.amount_value) / float(self.dollar_value)) * 976.39
                    self.naira_entry.delete(0, END)
                    self.naira_entry.insert(0, "₦" + str(self.naira_amount))
                if self.currency_value == "EURO" and self.trade_value == "BUY":
                    self.naira_amount = (float(self.amount_value) / float(self.dollar_value)) * 835.46
                    self.naira_entry.delete(0, END)
                    self.naira_entry.insert(0, "₦" + str(self.naira_amount))
                if self.currency_value == "EURO" and self.trade_value == "SELL":
                    self.naira_amount = (float(self.amount_value) / float(self.dollar_value)) * 835.46
                    self.naira_entry.delete(0, END)
                    self.naira_entry.insert(0, "₦" + str(self.naira_amount))
                if self.currency_value == "YEN" and self.trade_value == "BUY":
                    self.naira_amount = (float(self.amount_value) / float(self.dollar_value)) * 5.25
                    self.naira_entry.delete(0, END)
                    self.naira_entry.insert(0, "₦" + str(self.naira_amount))
                if self.currency_value == "YEN" and self.trade_value == "SELL":
                    self.naira_amount = (float(self.amount_value) / float(self.dollar_value)) * 5.25
                    self.naira_entry.delete(0, END)
                    self.naira_entry.insert(0, "₦" + str(self.naira_amount))
                if self.currency_value == "FRANC" and self.trade_value == "BUY":
                    self.naira_amount = (float(self.amount_value) / float(self.dollar_value)) * 871.35
                    self.naira_entry.delete(0, END)
                    self.naira_entry.insert(0, "₦" + str(self.naira_amount))
                if self.currency_value == "FRANC" and self.trade_value == "SELL":
                    self.naira_amount = (float(self.amount_value) / float(self.dollar_value)) * 871.35
                    self.naira_entry.delete(0, END)
                    self.naira_entry.insert(0, "₦" + str(self.naira_amount))
                if self.currency_value == "RAND" and self.trade_value == "BUY":
                    self.naira_amount = (float(self.amount_value) / float(self.dollar_value)) * 40.37
                    self.naira_entry.delete(0, END)
                    self.naira_entry.insert(0, "₦" + str(self.naira_amount))
                if self.currency_value == "RAND" and self.trade_value == "SELL":
                    self.naira_amount = (float(self.amount_value) / float(self.dollar_value)) * 40.37
                    self.naira_entry.delete(0, END)
                    self.naira_entry.insert(0, "₦" + str(self.naira_amount))
                if self.currency_value == "RUBLE" and self.trade_value == "BUY":
                    self.naira_amount = (float(self.amount_value) / float(self.dollar_value)) * 8.14
                    self.naira_entry.delete(0, END)
                    self.naira_entry.insert(0, "₦" + str(self.naira_amount))
                if self.currency_value == "RUBLE" and self.trade_value == "SELL":
                    self.naira_amount = (float(self.amount_value) / float(self.dollar_value)) * 8.14
                    self.naira_entry.delete(0, END)
                    self.naira_entry.insert(0, "₦" + str(self.naira_amount))
                if self.currency_value == "CEDI" and self.trade_value == "BUY":
                    self.naira_amount = (float(self.amount_value) / float(self.dollar_value)) * 67.87
                    self.naira_entry.delete(0, END)
                    self.naira_entry.insert(0, "₦" + str(self.naira_amount))
                if self.currency_value == "CEDI" and self.trade_value == "SELL":
                    self.naira_amount = (float(self.amount_value) / float(self.dollar_value)) * 67.87
                    self.naira_entry.delete(0, END)
                    self.naira_entry.insert(0, "₦" + str(self.naira_amount))

        def reset_button(self):
            self.combo_currency.delete(0, END)
            self.combo_trade.delete(0, END)
            self.dollar_entry.delete(0, END)

            self.amount_entry.delete(0, END)
            self.naira_entry.delete(0, END)

        def currency_info(self):
            messagebox.showinfo("Info", "Choose the currency you'd like to trade from the dropdown list")

        def b_s_info(self):
            messagebox.showinfo("Info", "Select whether you'd like to buy or sell this currency")

        def dollar_info(self):
            messagebox.showinfo("Info", "Displays rate in $ dollar")

        def amount_info(self):
            messagebox.showinfo("Info", "Enter amount you'd want to trade")

    exchange_app = Exchange_calculator(calc_window)
    exchange_app.mainloop()


splash_screen = Tk()
splash_screen.overrideredirect(True)

img = Image.open("cash.jpg")
splash_width = 300
splash_height = 200
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
