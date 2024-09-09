import tkinter as Tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from colorthief import ColorThief
import os

root = Tk()
root.title("Color picker from image")
root.geometry("800x470+100+100")
root.configure(bg="#e4e8eb")
root.resizable(False, False)

def showimage():
    global filename
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title='Select Image File',
        filetypes=(('PNG file', '*.png'),
                   ('JPG file', '*.jpg'),
                   ('All files', '*.*'))
    )
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img, width=310, height=270)
    lbl.image = img

def Findcolor():
    ct = ColorThief(filename)
    palette = ct.get_palette(color_count=10)  # Use 10 colors to match with the number of colors displayed

    # Ensure palette has exactly 10 colors
    if len(palette) < 10:
        palette.extend([(0, 0, 0)] * (10 - len(palette)))  # Extend palette if there are fewer than 10 colors

    # Extract colors and convert them to hex
    hex_colors = [f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}" for color in palette]

    # Update color displays
    for i, color in enumerate(hex_colors):
        if i < 5:
            colors.itemconfig(ids[i], fill=color)
            hex_labels[i].config(text=color)
        else:
            colors2.itemconfig(ids2[i - 5], fill=color)
            hex_labels2[i - 5].config(text=color)

# Icon
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

Label(root, width=120, height=10, bg="#4272f9").pack()

# Frame
frame = Frame(root, width=700, height=370, bg="#fff")
frame.place(x=50, y=50)

logo = PhotoImage(file="logo.png")
Label(frame, image=logo, bg="#fff").place(x=10, y=10)

Label(frame, text="Color Finder", font="arial 25 bold", bg="white").place(x=100, y=20)

# Color1
colors = Canvas(frame, bg="#fff", width=150, height=265, bd=0)
colors.place(x=20, y=90)

ids = [
    colors.create_rectangle((10, 10, 50, 50), fill="#b8255f"),
    colors.create_rectangle((10, 50, 50, 100), fill="#db4035"),
    colors.create_rectangle((10, 100, 50, 150), fill="#ff9933"),
    colors.create_rectangle((10, 150, 50, 200), fill="#fad000"),
    colors.create_rectangle((10, 200, 50, 250), fill="#afb83b")
]

hex_labels = [
    Label(colors, text="#b8255f", fg="#000", font="arial 12 bold", bg="white"),
    Label(colors, text="#db4035", fg="#000", font="arial 12 bold", bg="white"),
    Label(colors, text="#ff9933", fg="#000", font="arial 12 bold", bg="white"),
    Label(colors, text="#fad000", fg="#000", font="arial 12 bold", bg="white"),
    Label(colors, text="#afb83b", fg="#000", font="arial 12 bold", bg="white")
]

for i, label in enumerate(hex_labels):
    label.place(x=60, y=15 + i * 50)

# Color2
colors2 = Canvas(frame, bg="#fff", width=150, height=265, bd=0)
colors2.place(x=180, y=90)

ids2 = [
    colors2.create_rectangle((10, 10, 50, 50), fill="#7ecc49"),
    colors2.create_rectangle((10, 50, 50, 100), fill="#299438"),
    colors2.create_rectangle((10, 100, 50, 150), fill="#6accbc"),
    colors2.create_rectangle((10, 150, 50, 200), fill="#158fad"),
    colors2.create_rectangle((10, 200, 50, 250), fill="#14aaf5")
]

hex_labels2 = [
    Label(colors2, text="#7ecc49", fg="#000", font="arial 12 bold", bg="white"),
    Label(colors2, text="#299438", fg="#000", font="arial 12 bold", bg="white"),
    Label(colors2, text="#6accbc", fg="#000", font="arial 12 bold", bg="white"),
    Label(colors2, text="#158fad", fg="#000", font="arial 12 bold", bg="white"),
    Label(colors2, text="#14aaf5", fg="#000", font="arial 12 bold", bg="white")
]

for i, label in enumerate(hex_labels2):
    label.place(x=60, y=15 + i * 50)

# Select image
selectimege = Frame(frame, width=340, height=350, bg="#d6dee5")
selectimege.place(x=350, y=10)

f = Frame(selectimege, bd=3, bg="black", width=320, height=280, relief=GROOVE)
f.place(x=10, y=10)

lbl = Label(f, bg="black")
lbl.place(x=0, y=0)

Button(selectimege, text="Select Image", width=12, height=1, font="arial 14 bold", command=showimage).place(x=10, y=300)
Button(selectimege, text="Find Color", width=12, height=1, font="arial 14 bold", command=Findcolor).place(x=176, y=300)

root.mainloop()
