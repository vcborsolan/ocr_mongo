import os
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from pdf2image import convert_from_path

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """

    pages = convert_from_path(filename)
    image_counter = 1
    file_path = filename.split('/')[2].split('.')[0]
    
    if not os.path.exists("static/pdf/"+file_path):
        os.makedirs("static/pdf/"+file_path)

    for page in pages:

        filename = "static/pdf/"+file_path+"/page_"+str(image_counter)+".jpg"
        page.save(filename , 'JPEG')
        print(image_counter)
        image_counter = image_counter + 1

        text = []
    for i in range(1, image_counter):

        text.append(str(pytesseract.image_to_string(Image.open("static/pdf/"+file_path+"/page_"+str(i)+".jpg"), lang='por')))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

# print(ocr_core('static/img/Placa_EWU2731.pdf'))
# print(pytesseract.image_to_data(Image.open('static/img/cupom_real.jpeg'), lang='por'))