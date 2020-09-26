import io
import os
import googletrans

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
