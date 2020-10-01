###############################
#LANCELOTXV
###############################

import pytesseract
from PIL import Image
import cv2
import numpy as np
from pytesseract import Output
from textblob import TextBlob


from pdf2image import convert_from_path
dpi = 500 # dots per inch
pdf_file = 'pdf-sample.pdf'
pages = convert_from_path(pdf_file ,dpi )
for i in range(len(pages)):
   page = pages[i]
   page.save('output_{}.jpg'.format(i), 'JPEG')

text = ""

for i in range(len(pages)-1):
    file_path= 'output_{}.jpg'.format(i)
    im = Image.open(file_path)    
    
    from pytesseract import image_to_string
    text = text + image_to_string(im,lang = 'eng')
    with open('Output.txt', 'w',5 ,'utf-8') as text_file:
        text_file.write(text)


#FOR LANGUAGES OTHER THAN ENGLISH#

tb = TextBlob(text)
translated = tb.translate(to='eng')
print(translated)

text = str(translated)

##################################


with open('Output.txt', 'w',5 ,'utf-8') as text_file:
    text_file.write(test)


with open('Output.txt', 'r') as txtin:
    lines = txtin.read().splitlines(True)
with open('Output.txt', 'w') as txtout:
    txtout.writelines(lines[8:-8])


from gtts import gTTS 
import os 

file = open("Output.txt", "r").read().replace("\n", " ")

language = 'en'

myobj = gTTS(text=str(file), lang=language, slow=False) 
myobj.save("TRANSLATION.mp3") 












