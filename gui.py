#GUI to ask user what language they speak, so we can translate image text to their language
from tkinter import *
import os
import sys
import shutil

window = Tk()
window.geometry("500x500")
window.title("Menu Translator")



def UploadAction(event=None):
    from tkinter import filedialog
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    # os.rename(filename, 'Users\Documents\GitHub\ShellHacks-Repo\resources')
    destination = os.path.abspath('resources')
    shutil.move(filename, destination)

def Translate():
    os.system('python main.py')

def show():
    myLabel = Label(window, text=clicked.get()).pack()

clicked = StringVar()
clicked.set("English")

drop = OptionMenu(window, clicked, "English", "Spanish", "French", "Italian", "Portuguese", "German", "Russian", "Arabic", "Vietnamese", "Filipino")
drop.pack()

menuButton = Button(window, text="Show Selection", command=show).pack()

label1 = Label(window, text="Welcome to our Menu Translator!", font=("arial", 16, "bold")).pack()
label2 = Label(window, text="Please upload a picture of the menu you want translated", font=("arial", 10)).pack()

buttonUpload = Button(window, text='Open', command=UploadAction).pack()
button1 = Button(window, text = "Translate", command=Translate).pack()
# button1.place(x=500, y=110)

window.mainloop()