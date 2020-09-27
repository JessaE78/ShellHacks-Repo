#GUI to ask user what language they speak, so we can translate image text to their language
from tkinter import *
from main import translate_image
from lang_code import *
import os
import sys
import shutil

window = Tk()
window.geometry("500x500")
window.title("Menu Translator")


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
drop = OptionMenu(window, clicked, *lang_tuple, command = set_lang)
drop.pack()

label1 = Label(window, text="Welcome to our Menu Translator!", font=("arial", 16, "bold")).pack()
label2 = Label(window, text="Please upload a picture of the menu you want translated", font=("arial", 10)).pack()

pronunciation = Checkbutton(window, text="Show Pronunciation Instead", variable=use_pronunciation, onvalue = True, offvalue = False).pack()

buttonUpload = Button(window, text='Open', command=UploadAction).pack()
button1 = Button(window, text = "Translate", command=Translate).pack()

window.mainloop()
