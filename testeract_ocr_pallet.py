import openpyxl
from PIL import Image
import pytesseract


file_path = r'.\OCR Teseract\PT-XUS181A.xlsx'
sheet_name = "Patrón de paletizado"
wb = openpyxl.load_workbook(file_path, keep_links=False)
sheet = wb[sheet_name]

images = []
for drawing in sheet._images:
    images.append(drawing)

if len(images) >= 2:
    image = images[1]
    if hasattr(image, 'image'):
        img_ref = image.image
        img = Image.open(img_ref.blob)
        img_format = img.format
        if img_format == 'WMF':
            print("WMF format is not supported directly; please convert manually.")
        else:
            img.save('extracted_image.png')  
            print("Image saved successfully.")
    else:
        print("No accessible image attribute.")
else:
    print("Not enough images found in the sheet.")
    
try:
    extracted_text = pytesseract.image_to_string('extracted_image.png')
    print("Extracted Text:")
    print(extracted_text)
except FileNotFoundError:
    print("Image file not found; check the previous steps.")
