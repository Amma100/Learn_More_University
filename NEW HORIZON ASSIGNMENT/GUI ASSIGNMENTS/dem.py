from tkinter import *

from PIL import Image, ImageTk


def create_circle(canvas, x, y, radius, **kwargs):
    return canvas.create_oval(x - radius, y - radius, x + radius, y + radius, **kwargs)


window = Tk()

background_image = Image.open("casino1.jpg")
background_photo = ImageTk.PhotoImage(background_image)

canvas = Canvas(window, width=160, height=180)
canvas.create_image(0, 0, anchor=NW, image=background_photo)
canvas.pack()

circle_x = 80
circle_y = 55
circle_rad = 50
circle_color = "blue"

circle = create_circle(canvas, circle_x, circle_y, circle_rad, fill=circle_color)

label = Label(canvas, text="Circle Label", bg=circle_color, fg="white")
label.place(x=circle_x, y=circle_y, anchor="center")

window.mainloop()
