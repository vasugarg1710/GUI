from tkinter import *
root = Tk()
f1 = Frame()
label1 = Label(f1,text="Welcome to Pycharm",bg="grey",pady=50,font="comicsans 20 bold",fg="red",borderwidth=6,relief=SUNKEN)


f2 = Frame()
label2 = Label(f2,text="Side bar",font="comicsans 20 bold",fg="white",bg="grey",pady=400,relief=SUNKEN,borderwidth=6)
label2.pack()
f2.pack(side=LEFT)
label1.pack(fill="x")
f1.pack(side=TOP,fill="x")

root.mainloop()