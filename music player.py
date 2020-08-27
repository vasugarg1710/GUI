from tkinter import *
from tkinter.filedialog import askopenfile
from pygame import mixer
from tkinter import messagebox as mb
root = Tk()
root.title("Music player by Vasu")
root.minsize(510,350)
root.maxsize(510,350)
def openfile():
    song = askopenfile(filetypes =[('Music Files', '*.mp3')])
    mixer.init()
    mixer.music.load(song)
    mixer.music.play()
    mb.showinfo("Playing song",song.name)


text = Label(text="Music player",font="comicsans 35 bold",justify="center")
text3 = Label(text="by Vasu",font="comicsans 33 bold",justify="center")
add_btn = Button(text="Add music",font="comicsans 20",justify="center",pady="15",command=openfile)
stop_btn = Button(text="Stop music",font="comicsans 20",justify="center",pady="15",command=mixer.music.stop)
pause_btn = Button(text="Pause music",font="comicsans 20",justify="center",pady="15",command=mixer.music.pause)
resume_btn = Button(text="Resume music",font="comicsans 20",justify="center",pady="15",command=mixer.music.unpause)
footer = Label(text="@bestMusicPlayer ever",pady=5,font="comicsans 20",fg="green")


text.grid(row=0,column=0,pady=10)
text3.grid(row=0,column=1,pady=10)
add_btn.grid(row=1,column=0,pady=10)
stop_btn.grid(row=1,column=1,pady=10)
pause_btn.grid(row=2,column=0,pady=10)
resume_btn.grid(row=2,column=1,pady=10)
footer.grid(row=4)

root.mainloop()