import os
try:
    from PIL import Image as Image
except ImportError:
    import Image
import pytesseract

from wand.image import Image as Imagex


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """

    image_counter = 1
    file_path = filename.filename.split('.')[0]
    
    if not os.path.exists("static/pdf/"+file_path):
        os.makedirs("static/pdf/"+file_path)

    with(Imagex(filename=f"static/pdf/{file_path}.pdf" , resolution=120)) as source:
        images = source.sequence
        pages = len(images)
        for i in range(pages):
            filename_new = "static/pdf/"+file_path+"/page"+str(image_counter)+".jpg"
            Imagex(images[i]).save(filename=filename_new)
            image_counter = i + 1

    text = []
    for i in range(pages):
        text.append(str(pytesseract.image_to_string(Image.open("static/pdf/"+file_path+"/page"+str(i+1)+".jpg"), lang='por')))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

# print(ocr_core('static/img/certificado.pdf'))