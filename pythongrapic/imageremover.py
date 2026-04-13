from PIL import Image 
from rembg import remove

input_img = r"C:\Users\Lenovo\PycharmProjects\seyampythonproject\pythongrapic\WhatsApp Image 2025-10-28 at 23.13.38.jpeg"

input_img_open = Image.open (r"C:\Users\Lenovo\PycharmProjects\seyampythonproject\pythongrapic\WhatsApp Image 2025-10-28 at 23.13.38.jpeg")

output_img = remove (input_img_open)

output_img.save (r"C:\Users\Lenovo\PycharmProjects\seyampythonproject\pythongrapic\output_image.png")

print ("process completed successfully")

