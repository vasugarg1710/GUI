from tkinter import *
root = Tk()
root.geometry("400x300")
root.minsize(400,300)
label = Label(text="Ready",bg="green",fg="white",padx=1000,pady=2,font="comicsans 15")
label.pack(side=BOTTOM,anchor="se")
root.mainloop()