from tkinter import *
import os
from PIL import Image, ImageTk
root = Tk()
images = os.listdir()
imglist = [x for x in images if x.lower().endswith(".png")]
photolist = []
for index, image in enumerate(imglist):
    photo_file = Image.open(image)
    photo_file = photo_file.resize((150, 150))
    photo = ImageTk.PhotoImage(photo_file)
    photolist.append(photo)
    label = Label(image=photo)
    label.pack()
    print("reached here with "+image)

root.mainloop()