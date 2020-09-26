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
file_name = os.path.abspath('resources/italian_menu_test.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
text_anno = client.text_detection(image=image).text_annotations
with open('test.txt', 'w', encoding = 'utf-8') as f:
    f.write(str(text_anno))
separated_text = text_anno[0].description.split('\n')
separated_text.pop() #Get rid of last element, which is nothing

text_index = 1
#for text in separated_text:

translated = translator.translate(text_anno[0].description, src = text_anno[0].locale, dest = 'es')
translated_text_separated = translated.text.split('\n')
image = Image.open(file_name)
draw = ImageDraw.Draw(image)
#print(translated_text_separated)
for i in range(len(separated_text)):
    #Get the number of words
    text_num_words = len(separated_text[i].split(' '))
    #print(text_num_words)

    #Get the verticies of the first and last word of the portion being translated
    verts_first_word = text_anno[text_index].bounding_poly.vertices
    verts_last_word = text_anno[text_index + text_num_words - 1].bounding_poly.vertices
    #Crop and blur portion that's being translated
    cropped_img = image.crop((verts_first_word[0].x,verts_first_word[0].y,verts_last_word[2].x,verts_last_word[2].y))
    #blurred_img = cropped_img.filter(ImageFilter.GaussianBlur(radius=8))
    image.paste(cropped_img, (verts_first_word[0].x,verts_first_word[0].y))

    #Set font size to the size of original text
    font_type = ImageFont.truetype('fonts/times.ttf', verts_last_word[2].y - verts_first_word[0].y + 1)
    #Draw outline of text
    draw.text(xy = (verts_first_word[0].x - 1, verts_first_word[0].y), text=translated_text_separated[i], fill=(0,0,0), font = font_type)
    draw.text(xy = (verts_first_word[0].x + 1, verts_first_word[0].y), text=translated_text_separated[i], fill=(0,0,0), font = font_type)
    draw.text(xy = (verts_first_word[0].x, verts_first_word[0].y - 1), text=translated_text_separated[i], fill=(0,0,0), font = font_type)
    draw.text(xy = (verts_first_word[0].x, verts_first_word[0].y + 1), text=translated_text_separated[i], fill=(0,0,0), font = font_type)
    #Write translated text
    draw.text(xy = (verts_first_word[0].x, verts_first_word[0].y), text=translated_text_separated[i], fill=(255,255,255), font = font_type)

    text_index += text_num_words

print("Finished")
image.show()

