import os
import re
from tkinter import *
from tkinter import filedialog, messagebox

from PIL import Image, ImageTk


# display a splash screen before Notepro runs
def close_splash_screen():
    splash_screen.destroy()

    # configure my display window
    window = Tk()
    window.title("Untitled-Notepro")
    win_wid = 1215
    win_hig = 680
    window.config(bg="white")
    scr_wid = window.winfo_screenwidth()
    scr_hig = window.winfo_screenheight()
    x_coordinate = (scr_wid - win_wid) // 2
    y_coordinate = (scr_hig - win_hig) // 2
    window.geometry(f"{win_wid}x{win_hig}+{x_coordinate}+{y_coordinate}")
    img = PhotoImage(file="notedia1.png")
    window.iconphoto(False, img)

    # Inherit the frame class properties and methods to my Notepad_app
    class Notepro_app(Frame):
        def __init__(self, master):
            super().__init__(master)
            self.create_notepad_widget()

        def create_notepad_widget(self):
            # create a menu bar
            self.menu_bar = Menu(window)

            # configure the menu bar to the window toplevel
            window.config(menu=self.menu_bar)

            # add a file menu bar to the menu bar
            self.file_menu = Menu(self.menu_bar, tearoff=0)
            self.file_menu.add_command(label="New File", command=self.new_file)
            self.file_menu.add_command(label="Save", command=self.save_file)
            self.file_menu.add_command(label="Save As", command=self.save_file_as)

            # add an edit menu bar to the menu bar
            self.edit_menu = Menu(self.menu_bar, tearoff=0)
            self.edit_menu.add_command(label="Cut    ", command=self.cut)
            self.edit_menu.add_command(label="Copy", command=self.copy)
            self.edit_menu.add_command(label="Paste", command=self.paste)

            # add a format menu bar to the menu bar
            self.format_menu = Menu(self.menu_bar, tearoff=0)
            self.format_menu.add_command(label="Bold   ", command=self.bold)
            self.format_menu.add_command(label="Italic", command=self.italic)

            # add a help menu bar to the menu bar
            self.help_menu = Menu(self.menu_bar, tearoff=0)
            self.help_menu.add_command(label="About Notepro", command=self.about)

            # cascade all the menu bars in the menu bar
            self.menu_bar.add_cascade(label="File", menu=self.file_menu)
            self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
            self.menu_bar.add_cascade(label="Format", menu=self.format_menu)
            self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

            # create a text_area for inputting characters
            self.text_area = Text(window, wrap="word", font=("Arial", 12), borderwidth=0)

            # create a vertical and horizontal scroll bar for easy navigation of text area

            self.y_scroll = Scrollbar(window, command=self.text_area.yview)
            self.x_scroll = Scrollbar(window, command=self.text_area.xview, orient=HORIZONTAL)

            # configure the scroll bars to the text area
            self.text_area.config(xscrollcommand=self.x_scroll.set, yscrollcommand=self.y_scroll.set)

            # add pack
            self.x_scroll.pack(side=BOTTOM, fill=X)
            self.y_scroll.pack(side=RIGHT, fill=Y)
            self.text_area.pack(side=LEFT, fill=BOTH, expand=True)

        # define a function for a new notepad text area
        def new_file(self):
            # ask a question to the user
            file_txt = messagebox.askyesnocancel("Notepad", "Do you want to save changes?")
            # if user clicks cancel
            if file_txt is None:
                messagebox.showinfo("Notepro", "Operation canceled")
            # if user clicks yes
            elif file_txt:
                val = self.text_area.get("1.0", "end-1c")
                print(val)
                # if notepro text area is empty
                if val == "":
                    messagebox.showerror("Notepro", "No changes made")
                # if notepro text area is not empty
                else:
                    file_dir_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                                 filetypes=[("Text Files", "*.txt")])
                    if file_dir_path:
                        regex_file_name = re.findall("\w{1,20}", file_dir_path)
                        file_name = regex_file_name[10]
                        print(regex_file_name)
                        print(file_name)
                        window.title("Untitled-Notepro")
                        with open(file_dir_path, "w") as file:
                            file.write(self.text_area.get("1.0", "end-1c"))
                            self.text_area.delete("1.0", "end-1c")
            # if user clicks no
            else:
                messagebox.showinfo("Notepro", "Changes will not be saved.")
                self.text_area.delete("1.0", "end-1c")
                window.title("Untitled-Notepro")

        # define a function to save file
        def save_file(self):
            title_name = window.title()
            word = title_name.split("-")
            value = word[0]
            print(title_name)
            print(word)
            print(value)
            val = value + ".txt"
            print(val)
            if os.path.isfile(val):  # run if the file is already saved on the system
                with open(val, "w") as file:
                    file.write(self.text_area.get("1.0", "end-1c"))
            else:  # run if the file is not saved on the system
                file_dir_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                             filetypes=[("Text Files", "*.txt")])
                regex_file_name = re.findall("\w{1,20}", file_dir_path)
                file_name = regex_file_name[10]
                print(regex_file_name)
                print(file_name)
                if file_dir_path:
                    window.title(f"{file_name}-Notepro")
                    with open(file_dir_path, "w") as file:
                        file.write(self.text_area.get("1.0", "end-1c"))

        # define a function to save file as....
        def save_file_as(self):
            file_dir_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
            if file_dir_path:
                regex_file_name = re.findall("\w{1,20}", file_dir_path)
                file_name = regex_file_name[10]
                print(regex_file_name)
                print(file_name)
                window.title(f"{file_name}-Notepro")
                with open(file_dir_path, "w") as file:
                    file.write(self.text_area.get("1.0", "end-1c"))

        # define a function to cut characters from a text area
        def cut(self):
            # get the word that is selected
            self.word = self.text_area.selection_get()
            self.text_area.clipboard_clear()
            self.text_area.clipboard_append(self.word)
            # check if the text is not an empty string
            if self.word:
                self.text_area.delete("sel.first", "sel.last")

        # define a function to copy characters from a text area
        def copy(self):
            self.word = self.text_area.selection_get()
            self.text_area.clipboard_clear()
            self.text_area.clipboard_append(self.word)

        # define a function to paste characters from a text area
        def paste(self):
            self.clip_text = self.text_area.clipboard_get()
            self.text_area.insert(END, self.word)

        # define a function to bold a character or group of characters from a text area
        def bold(self):
            self.char_first_index = self.text_area.index(SEL_FIRST)
            self.char_last_index = self.text_area.index(SEL_LAST)
            self.text_area.tag_configure("bold", font=("Arial", 10, "bold"))
            self.text_area.tag_add("bold", self.char_first_index, self.char_last_index)

        # define a function to italic a character or group of characters from a text area
        def italic(self):
            self.char_first_index = self.text_area.index(SEL_FIRST)
            self.char_last_index = self.text_area.index(SEL_LAST)
            self.text_area.tag_configure("italic", font=("Arial", 10, "italic"))
            self.text_area.tag_add("italic", self.char_first_index, self.char_last_index)

        # define a close function
        def close(self):
            self.message.destroy()

        # define a function to display an "about" message information

        def about(self):
            self.message = Tk()
            self.message.config(bg="gray10")
            self.message.overrideredirect(True)
            msg_wid = 600
            msg_hig = 270
            scrn_wid = self.message.winfo_screenwidth()
            scrn_hig = self.message.winfo_screenheight()
            x_axis = (scrn_wid - msg_wid) // 2
            y_axis = (scrn_hig - msg_hig) // 2
            self.message.geometry(f"{msg_wid}x{msg_hig}+{x_axis}+{y_axis}")
            about_label = Label(self.message, text="About Notepro", font=("Brush script MT", 35, "bold"), fg="#AEABD6",
                                bg="gray10")
            about_label.place(x=190)
            msg_body_label1 = Label(self.message,
                                    text="Notepro v.1.0 is a user friendly desktop notebook that is designed for text writing",
                                    font=("Arial", 12), bg="gray10", fg="white")
            msg_body_label1.place(x=20, y=70)
            msg_body_label2 = Label(self.message, text="and easy manipulation of files.", font=("Arial", 12),
                                    bg="gray10", fg="white")
            msg_body_label2.place(x=180, y=100)
            msg_body_label3 = Label(self.message, text="Developed by Anyim Amarachi",
                                    font=("Brush script MT", 30, "bold"), bg="gray10", fg="#AEABD6")
            msg_body_label3.place(x=70, y=160)
            close_label = Button(self.message, text="Close", font=("Arial", 12, "bold"), relief="flat", bg="red",
                                 fg="white", activebackground="black", command=self.close)
            close_label.place(x=530, y=225)
            self.message.mainloop()

    note_app = Notepro_app(window)
    note_app.mainloop()


# create an instance of Tk
splash_screen = Tk()

# override window widgets
splash_screen.overrideredirect(True)

# set splash screen width and heihgt
s_scr_wid = 400
s_scr_hig = 300

# open an image using the PIL module
image = Image.open("note1.jpg")
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
notepro_label = Label(splash_screen, text="Notepro", font=("Brush script MT", 70, "bold"), bg="white", fg="#AEABD6")
notepro_label.place(x=80, y=90)

# close the splash screen after 2 sec
splash_screen.after(2000, close_splash_screen)
splash_screen.mainloop()
