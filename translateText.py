import cv2
import pytesseract
import matplotlib.pyplot as plt
from PIL import Image

image = cv2.imread("D:\Repository\Python\translate_py\files\test.jpg")

string = pytesseract.image_to_string(image)
print(string)