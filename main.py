import io
import os
import googletrans

#Pillow Library that allows for image manipulation
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from googletrans import Translator


translator = Translator()
#sets up GOOGLE_APPLICATION_CREDENTIALS 
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'shell_hacks.json'

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath('wakeupcat.jpg')
text =open("test.txt","w")

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)
    text.write(label.description + "\n")

text = open("test.txt","r")

print('\n')
print('Translated Version: ')
text_contents = text.read()
translated_version = translator.translate(text_contents, dest ='spanish')
print(translated_version.text)

image = Image.open('wakeupcat.jpg')
#Download a font to use

cropped_image = image.crop((30,390,580,470))
blurred_image = cropped_image.filter(ImageFilter.GaussianBlur(radius=8))
image.paste(blurred_image,(30,390,580,470))

font_type = ImageFont.truetype('Arial.ttf', 48)

draw = ImageDraw.Draw(image)
draw.text(xy=(150,400),text="BIG FAT CAT", fill=(255,0,0),font=font_type)
image.show()
