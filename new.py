from tkinter import *
root = Tk()
root.title("My form")
root.geometry("500x200")
root.minsize(500,200)
root.maxsize(500,200)
def getval():
    print(f"It works. Username is {uservalue.get()} and password is {passvalue.get()}")
Label(text="Welcome to our form", font="comicsans 20 bold underline",pady=15).grid()
username = Label(text="username",font="comicsans 15")
password = Label(text="password",font="comicsans 15")

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(textvariable=uservalue)
passentry = Entry(textvariable=passvalue)

username.grid(row=1,column=0)
password.grid(row=2,column=0)
userentry.grid(row=1,column=1)
passentry.grid(row=2,column=1)
Button(text="Submit",font="comicsans 15",command=getval).grid(pady=10)
root.mainloop()