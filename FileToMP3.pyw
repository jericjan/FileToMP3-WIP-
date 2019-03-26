from tkinter import *
import subprocess
import os

win = Tk()

win.title("FILE CONVERTER by Jeric")
win.geometry("350x180")
win.resizable(False, False)

def copy():
    oldname = OneBox.get()
    newname = TwoBox.get()
    subprocess.call(["ffmpeg", "-i", oldname, "-b:a", "320k", newname])
    print("DONE, BOIIIIII!!!")

def closeapp():
    sys.exit()

subprocess.call('color 0a', shell=True)
titleLabel = Label(win, text="PUT ME IN THE SAME FOLDER AS YOUR FILES!")
titleLabel.grid(row=0, column=0, sticky=W)
oneLabel = Label(win, text="What's your file name? (with extension name)")
oneLabel.grid(row=1, column=0, sticky=W)
OneBox = Entry(win, width=50)
OneBox.grid(row=2, column=0, sticky=W)

twoLabel = Label(win, text="What's your new file name? (with .mp3)")
twoLabel.grid(row=3, column=0, sticky=W)
TwoBox = Entry(win, width=50)
TwoBox.grid(row=4, column=0, sticky=W)

goButton = Button(win, text="GO!", command = copy)
goButton.grid(row=5, column=0, sticky=W)

threeLabel = Label(win, text= "El Psy Kongroo...")
threeLabel.grid(row=6, column=0,sticky=W)

exitButton = Button(win, text="EXIT", command = closeapp)
exitButton.grid(row=7, column=1, sticky=W)

win.mainloop()
