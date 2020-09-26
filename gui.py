#GUI to ask user what language they speak, so we can translate image text to their language
from tkinter import *
import os
import sys

window = Tk()
window.geometry("500x500")
window.title("Menu Translator")

def UploadAction(event=None):
    from tkinter import filedialog
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

def Translate():
    os.system('python main.py')

label1 = Label(window, text = "Welcome to our Menu Translator!", font = ("arial", 16, "bold")).pack()

label2 = Label(window, text = "Please upload a picture of the menu you want translated", font = ("arial", 10)).pack()

buttonUpload = Button(window, text='Open', command=UploadAction).pack()
button1 = Button(window, text = "Translate", fg = "black", bg = "white", command=Translate).pack()
# button1.place(x=500, y=110)

window.mainloop()