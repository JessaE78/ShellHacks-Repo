def check_coords(tl_coord, br_coord): #top left coord and bottom right coord
    '''
    Make sure that the top left coordinate is actually top left, and bottom right coord is actually bottom right
    '''
    if tl_coord.x > br_coord.x:
        tl_coord.x, br_coord.x = br_coord.x, tl_coord.x
    if tl_coord.y > br_coord.y:
        tl_coord.y, br_coord.y = br_coord.y, tl_coord.y
    return tl_coord, br_coord

def get_full_text_n_size(block):
    '''
    Get all of the text in a block and the text's height
    '''
    full_words = ""
    size = 0
    for paragraph in block.paragraphs:
        for word in paragraph.words:
            size = abs(word.bounding_box.vertices[0].y - word.bounding_box.vertices[2].y) #Get text height
            for symbol in word.symbols:
                full_words+=symbol.text
                break_type = symbol.property.detected_break.type
                if break_type == 1:
                    full_words+=" "
                elif break_type == 5 or break_type == 3:
                    full_words+="\n"
    full_words += "@"
    return full_words, size

import io
import os
import googletrans

#Pillow Library that allows for image manipulation
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from googletrans import Translator

def translate_image(image_file, dest_lang, do_pronunciation):
    translator = Translator()
    #sets up GOOGLE_APPLICATION_CREDENTIALS 
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'menuTranslatorAuthentication.json'
    # Instantiates a client and read the images
    client = vision.ImageAnnotatorClient()
    content = image_file.read()
    image = types.Image(content=content)

    # Performs text detection on the image file
    text_anno = client.text_detection(image=image)
    text_blocks = text_anno.full_text_annotation.pages[0].blocks
    text_to_translate = ""
    #Height of the text in each block
    text_sizes = []
    for block in text_blocks:
        text, text_size = get_full_text_n_size(block)
        text_to_translate+=text
        text_sizes.append(text_size)
    
    #Translate the text
    translated = translator.translate(text_to_translate, src = text_anno.text_annotations[0].locale, dest = dest_lang)
    #Split the text based on the separator used in get_full_text_n_size()
    translated_text_separated = translated.text.split('@')
    #Remove the empty last element
    translated_text_separated.pop()
    try:
        pronunciation = translated.extra_data["translation"][len(translated.extra_data["translation"]) - 1][3]
        pronunciation_separated = ""
        if (pronunciation != None):
            #Split the text based on the separator used in get_full_text_n_size()
            pronunciation_separated = pronunciation.split('@')
            #Remove the empty last element
            pronunciation_separated.pop()
        else: #This may occur when the original text is a latin-based langauge (English, spanish, etc)
            print("Pronunciation set to false because there is no available pronunciation")
            do_pronunciation = False
    except IndexError: #This may occur when the original text is a latin-based langauge (English, spanish, etc)
        print("Pronunciation set to false because there is no available pronunciation")
        do_pronunciation = False

    image = Image.open(image_file)
    draw = ImageDraw.Draw(image)
    #Begin bluring the original text and writing the translated text
    for i in range(min(len(translated_text_separated), len(text_blocks))): #min() to make sure we don't get out of index error
        #Get the verticies of the first and last word of the portion being translated
        top_left_vert = text_blocks[i].bounding_box.vertices[0]
        bot_right_vert = text_blocks[i].bounding_box.vertices[2]
        top_left_vert, bot_right_vert = check_coords(top_left_vert, bot_right_vert) #Make sure the coordinates are valid for cropping and blurring

        #Crop and blur portion that's being translated, then paste it back in
        cropped_img = image.crop((top_left_vert.x,top_left_vert.y,bot_right_vert.x,bot_right_vert.y))
        blurred_img = cropped_img.filter(ImageFilter.GaussianBlur(radius=8))
        image.paste(blurred_img, (top_left_vert.x,top_left_vert.y))

        #Set font size to the size of original text
        font_type = ImageFont.truetype('fonts/ARIALUNI.ttf', text_sizes[i])
        if do_pronunciation:
            #Draw outline of text
            draw.text(xy = (top_left_vert.x - 1, top_left_vert.y), text=pronunciation_separated[i], fill=(0,0,0), font = font_type)
            draw.text(xy = (top_left_vert.x + 1, top_left_vert.y), text=pronunciation_separated[i], fill=(0,0,0), font = font_type)
            draw.text(xy = (top_left_vert.x, top_left_vert.y - 1), text=pronunciation_separated[i], fill=(0,0,0), font = font_type)
            draw.text(xy = (top_left_vert.x, top_left_vert.y + 1), text=pronunciation_separated[i], fill=(0,0,0), font = font_type)
            #Write translated text
            draw.text(xy = (top_left_vert.x, top_left_vert.y), text=pronunciation_separated[i], fill=(255,255,255), font = font_type)
        else:
            #Draw outline of text
            draw.text(xy = (top_left_vert.x - 1, top_left_vert.y), text=translated_text_separated[i], fill=(0,0,0), font = font_type)
            draw.text(xy = (top_left_vert.x + 1, top_left_vert.y), text=translated_text_separated[i], fill=(0,0,0), font = font_type)
            draw.text(xy = (top_left_vert.x, top_left_vert.y - 1), text=translated_text_separated[i], fill=(0,0,0), font = font_type)
            draw.text(xy = (top_left_vert.x, top_left_vert.y + 1), text=translated_text_separated[i], fill=(0,0,0), font = font_type)
            #Write translated text
            draw.text(xy = (top_left_vert.x, top_left_vert.y), text=translated_text_separated[i], fill=(255,255,255), font = font_type)
    return image
