import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

image = Image.open('image_in_project')
text = pytesseract.image_to_string(image)
print(text)
