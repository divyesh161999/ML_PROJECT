from googletrans import Translator
from PIL import Image
import pytesseract
import cv2
import os
#image = cv2.imread("image.jpg")
from PIL import Image,ImageFilter
from googletrans import Translator
from PIL import Image
import pytesseract
import cv2
import os

im = Image.open('marathi.jpg')
   
from PIL import ImageEnhance  
enh = ImageEnhance.Contrast(im).enhance(1.20)
#enh.enhance(1.20).show("50% more contrast")
print(type(enh))
enh.save("rotated_picture.jpeg")
text = pytesseract.image_to_string(im, lang = 'mar')
print(text)
