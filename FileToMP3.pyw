from tkinter import *
import subprocess
import os
from tkinter import filedialog

win = Tk()

win.title("FILE2MP3 by Jeric")
win.geometry("300x180")
win.resizable(False, False)

def copy():
    dir1 = tempdir1.replace('/','\\')
    # dir2 = tempdir2.replace('/','\\')
    bdir1 = os.path.basename(dir1)
    bdir2 = os.path.splitext(os.path.basename(dir1))[0]

    oldname = str(bdir1)
    newname = str(bdir2) + ".mp3"
    # print("ffmpeg", "-i", oldname, "-b:a", "320k", newname)
    subprocess.call(["ffmpeg", "-i", oldname, "-b:a", "320k", newname])
    print("DONE, BOIIIIII!!!")
    donn = Label(win, text="DONE!!!", bg="black", fg="white")
    donn.grid(row=5, column=1, sticky=W)

def closeapp():
    sys.exit()

subprocess.call('color 0a', shell=True)
subprocess.call('echo MP4 files:', shell=True)
subprocess.call('dir /b *.mp4', shell=True)
subprocess.call('echo.', shell=True)
subprocess.call('echo MKV files:', shell=True)
subprocess.call('dir /b *.mkv', shell=True)
subprocess.call('echo.', shell=True)
subprocess.call('echo WEBM files:', shell=True)
subprocess.call('dir /b *.webm', shell=True)
subprocess.call('echo.', shell=True)
subprocess.call('echo M4A files:', shell=True)
subprocess.call('dir /b *.m4a', shell=True)
subprocess.call('echo.', shell=True)

titleLabel = Label(win, text="PUT ME IN THE SAME FOLDER AS YOUR FILES!")
titleLabel.grid(row=0, column=0, sticky=W)
oneLabel = Label(win, text="1. Select the file you want converted to mp3")
oneLabel.grid(row=1, column=0, sticky=W)

def search_for_file():
    currdir = os.getcwd()
    global tempdir1
    tempdir1 = filedialog.askopenfilename(parent=win, initialdir=currdir, title='Please select a directory', filetype= (("MP4", "*.mp4"), ("MKV", "*.mkv"), ("MEBM", "*.webm"), ("M4A", "*.m4a"),("All files", "*.*")))
    print("File to be converted is " + tempdir1)

def save_file():
    currdir = os.getcwd()
    global tempdir2
    tempdir2 = filedialog.asksaveasfilename(parent=win, initialdir=currdir, title='Please select a directory', filetype= (("MP3", "*.mp3"), ("All files", "*.*")))
    print("File to be saved is " +tempdir2)

browse_button = Button(win, text="Browse file!", command=search_for_file)
browse_button.grid(row=2, column=0, sticky=W)

""""OneBox = Entry(win, width=50)
OneBox.grid(row=2, column=0, sticky=W)"""
twoLabel = Label(win, text="2. PRESS GO!")
twoLabel.grid(row=3, column=0, sticky=W)

goButton = Button(win, text="GO!", command = copy)
goButton.grid(row=4, column=0, sticky=W)

threeLabel = Label(win, text= "El Psy Kongroo...")
threeLabel.grid(row=5, column=0,sticky=W)

exitButton = Button(win, text="EXIT", command = closeapp)
exitButton.grid(row=6, column=1, sticky=W)

win.mainloop()
