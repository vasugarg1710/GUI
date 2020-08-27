from tkinter import *
def clearTextInput():
    textArea.delete("1.0","end")
    root.title("Untitled - Notepad")
root = Tk()
root.title("Untitled - Notepad")
textArea = Text(font="comicsansms 20")
textArea.pack(fill=X)
menubar = Menu(root)
file = Menu(menubar, tearoff=0)
file.add_command(label="New",command=clearTextInput)
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as...")
file.add_command(label="Close")

file.add_separator()

file.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=file)
edit = Menu(menubar, tearoff=0)
edit.add_command(label="Undo")

edit.add_separator()

edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
edit.add_command(label="Delete")
edit.add_command(label="Select All")

menubar.add_cascade(label="Edit", menu=edit)
help = Menu(menubar, tearoff=0)
help.add_command(label="About")
menubar.add_cascade(label="Help", menu=help)

root.config(menu=menubar)

root.mainloop()