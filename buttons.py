from tkinter import *
root = Tk()
def show_b1():
    print("you clicked on button 1")
def show_b2():
    print("you clicked on button 2")
def show_b3():
    print("you clicked on button 3")

def show_b4():
    print("you clicked on button 4")
b1 = Button(text="Button 1",padx=5,pady=5,font="comicsans 15 bold",bg="green",fg="white",relief=SUNKEN,borderwidth=6,command=show_b1)
b1.pack(side="left",anchor="nw",padx=5,pady=5)
b2 = Button(text="Button 2",padx=5,pady=5,font="comicsans 15 bold",bg="green",fg="white",relief=SUNKEN,borderwidth=6,command=show_b2)
b2.pack(side="left",anchor="nw",padx=5,pady=5)
b3 = Button(text="Button 3",padx=5,pady=5,font="comicsans 15 bold",bg="green",fg="white",relief=SUNKEN,borderwidth=6,command=show_b3)
b3.pack(side="left",anchor="nw",padx=5,pady=5)
b4 = Button(text="Button 4",padx=5,pady=5,font="comicsans 15 bold",bg="green",fg="white",relief=SUNKEN,borderwidth=6,command=show_b4)
b4.pack(side="left",anchor="nw",padx=5,pady=5)

root.mainloop()