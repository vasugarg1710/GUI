from tkinter import *
from PIL import ImageTk,Image
import os
root = Tk()
files = os.listdir()
pngImages = [i for i in files if i.lower().endswith(".png")]
textFiles = [i for i in files if i.lower().endswith(".txt")]
photoList = []
total_content = []
for item in textFiles:
    with open(item) as f:
        content = f.read()
        total_content.append(content)
print(total_content)
print(pngImages)
print(textFiles)
labelPrim = Label(text="TIMES NEW ROMAN NEWSPAPER",font="comicsans 30 bold underline")
labelPrim.pack(side=TOP)
for index, image in enumerate(pngImages):
    photo_file = Image.open(image)
    photo_file = photo_file.resize((150, 150))
    photo = ImageTk.PhotoImage(photo_file)
    label2 = Label(text=total_content[index],font="comicsans 20 bold")
    photoList.append(photo)
    label = Label(image=photo)
    label2.pack(side=TOP, anchor="nw")
    label.pack(side=LEFT,anchor="nw",padx=10)
    print("reached here with "+image)
    # incase if text files are less than png files
    if index == len(total_content) - 1:
        break

root.mainloop()