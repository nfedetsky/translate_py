import cv2
import pytesseract
import easyocr
import matplotlib.pyplot as plt
from PIL import Image

img_file = 'D:/Repository/Python/translate_py/files/test.jpg'
f_file = 'D:/Repository/Python/translate_py/files/t2.txt'
img = Image.open(img_file)
pytesseract.pytesseract.tesseract_cmd = r'C://Program Files/Tesseract-OCR/tesseract.exe'

im_text = pytesseract.image_to_string(img, lang='rus')

print(im_text)

f = open(f_file, 'a')
f.write(im_text + '\n')
f.close()