#GUI to ask user what language they speak, so we can translate image text to their language
from tkinter import *
from main import translate_image
from lang_code import *
# from PIL import ImageTik, Image
import os
import sys
import shutil

window = Tk()
window.geometry("500x500")
window.title("Translator")
window.configure(bg="darkorchid1")


lang_tuple = []
for lang in LANGUAGES.values():
    lang_tuple.append(lang.capitalize())
lang_tuple = tuple(lang_tuple)

image = None
lang_code = "en"
use_pronunciation = BooleanVar()

def UploadAction(event=None):
    from tkinter import filedialog
    global image
    image = filedialog.askopenfile(mode='rb')
    print('Selected:', image.name)

def Translate():
    translated_img = translate_image(image, lang_code, use_pronunciation)

def set_lang(lang):
    lang = lang.lower()
    global lang_code
    lang_code = LANGCODES[lang]

def set_use_pronunciation(val):
    global use_pronunciation
    use_pronunciation = val

clicked = StringVar()
clicked.set("English")
drop = OptionMenu(window, clicked, *lang_tuple, command = set_lang).place(x=206, y=300)
#drop.pack()

label1 = Label(window, text="Welcome to our Translator!", font=("arial", 16, "bold")).pack()
label2 = Label(window, text="Please upload a picture you want translated", font=("Helvetica", 10)).pack()

pronunciation = Checkbutton(window, text="Show Pronunciation Instead", variable=use_pronunciation, onvalue = True, offvalue = False).place(x=160, y=365)

buttonUpload = Button(window, text='Open', command=UploadAction).place(x=230, y=80)
label3 = Label(window, text="Select the language you want your picture to be translated to").place(x=100, y=270)
button1 = Button(window, text = "Translate", command=Translate, bg="orchid1", fg="white").place(x=220, y=330)

window.mainloop()
