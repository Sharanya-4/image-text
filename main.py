from PIL import Image 
from pytesseract import pytesseract
# import os

path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

path_to_image = 'images/5.png'
# path_to_image = r'images/'

# for root,dirs,file_names in os.walk(path_to_image):
#     for file_name in file_names:
#         img = Image.open(path_to_image + file_name)

pytesseract.tesseract_cmd = path_to_tesseract
img = Image.open(path_to_image)
        # text = pytesseract.image_to_string(img)
        # print(text)
text = pytesseract.image_to_string(img)
print(text)



