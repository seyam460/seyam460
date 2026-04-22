from PIL import Image
import pytesseract

import_input = r"C:\Users\Lenovo\Downloads\text-photographed-eng.jpg"
input_image = Image.open(import_input)
text = pytesseract.image_to_string(input_image)
print(text)


