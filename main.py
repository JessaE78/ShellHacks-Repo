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
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'menuTranslatorAuthentication.json'

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath('resources/menu_test_1.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

text_response = client.text_detection(image=image)
text_anno = text_response.text_annotations
locale = text_anno[0].locale
separated_text = text_anno[0].description.split('\n')
separated_text.pop()

temp_counter = 1
text_dict = {}
#for text in separated_text:

image = Image.open('resources/menu_test_1.jpg')
draw = ImageDraw.Draw(image)
for text in separated_text:
    text_len = len(text.split(' '))
    text_dict[text] = temp_counter
    temp_counter += text_len

    print(text)
    translated_text = translator.translate(text, src = locale, dest = 'es')
    index = text_dict[text]
    print(index)
    verts_first_word = text_anno[index].bounding_poly.vertices
    verts_last_word = text_anno[index + text_len - 1].bounding_poly.vertices

    cropped_img = image.crop((verts_first_word[0].x,verts_first_word[0].y,verts_last_word[2].x,verts_last_word[2].y))
    blurred_img = cropped_img.filter(ImageFilter.GaussianBlur(radius=8))
    image.paste(blurred_img, (verts_first_word[0].x,verts_first_word[0].y,verts_last_word[2].x,verts_last_word[2].y))

    font_type = ImageFont.truetype('fonts/times.ttf', verts_last_word[2].y - verts_first_word[0].y)
    draw.text(xy = (verts_first_word[0].x, verts_first_word[0].y), text=translated_text.text, fill=(255,255,255), font = font_type)
image.show()
