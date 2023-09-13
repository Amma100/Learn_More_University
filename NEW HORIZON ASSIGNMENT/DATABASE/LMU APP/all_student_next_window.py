import sqlite3
import time
from tkinter import *


estu = Tk()
estu.config(bg="white")
estu.title("Students-Log")
msg_wid = 1215
msg_hig = 680
scrn_wid = estu.winfo_screenwidth()
scrn_hig = estu.winfo_screenheight()
x_axis = (scrn_wid - msg_wid) // 2
y_axis = (scrn_hig - msg_hig) // 2
estu.geometry(f"{msg_wid}x{msg_hig}+{x_axis}+{y_axis}")
pic = PhotoImage(file="lmu_logo.png")
estu.iconphoto(False, pic)


class AS(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.all_student_next()

    def all_student_next(self):

        self.menu_bar = Menu(estu)
        # create a text_area for inputting characters
        self.text_area = Text(estu, wrap="word", font=("Arial", 12), borderwidth=0)

        # create a vertical and horizontal scroll bar for easy navigation of text area

        self.y_scroll = Scrollbar(estu, command=self.text_area.yview)
        self.x_scroll = Scrollbar(estu, command=self.text_area.xview, orient=HORIZONTAL)

        # configure the scroll bars to the text area
        self.text_area.config(xscrollcommand=self.x_scroll.set, yscrollcommand=self.y_scroll.set)

        # add pack
        self.x_scroll.pack(side=BOTTOM, fill=X)
        self.y_scroll.pack(side=RIGHT, fill=Y)
        self.text_area.pack(side=LEFT, fill=BOTH, expand=True)

        conn = sqlite3.connect("Learn_More_University.db")

        try:

            cursor = conn.cursor()

            viewstudentsquery = "SELECT * FROM Students"

            result = cursor.execute(viewstudentsquery)
            conn.commit()

            for i in result:
                if result:
                    self.text_area.insert("end", f"\n                                                                                                                   {i[2]} {i[3]} DETAILS\n\n[STUDENT ID: {i[1]},   FIRST NAME: {i[2]},   LAST NAME: {i[3]},   AGE: {i[4]},   GENDER: {i[5]},   COURSE ENROLLED: {i[6]}]\n====================================================================================================================================\n\n")

        except sqlite3.Error as e:
            print("SQLite error:", e)
            conn.rollback()

        finally:
            conn.close()
        date = time.ctime()
        print("\nFile viewed at", date)


as_app = AS(estu)
as_app.mainloop()
