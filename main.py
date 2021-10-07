from document_scanner import documentScanner
from document_ocr import documentOCR
import os

# instantiate the documentScanner that is a child class
# of documentValidation class
scanner = documentScanner()

# define some valid formats for input photo that user
# can pass into the program
valid_formats = [".jpg", ".jpeg", ".jp2", ".png", ".bmp", ".tiff", ".tif"]

# define a base path for the input images
dir = "samples"

for filename in os.listdir(dir):
    # get the file extention from the input file and if the input format 
    # is in valid formats then grab the input file path, scan the image
    # using documentScanner class and then pass it into documentOCR 
    # function to OCR the input fields
    get_ext = lambda filename: os.path.splitext(filename)[1].lower()
    if  get_ext(filename) in valid_formats:
        img_path = dir + "/" + filename
        try:
            scanned_img = scanner.scan(img_path)
            documentOCR(scanned_img, filename)
        except Exception as e:
            print("SYSTEM ERROR : ", e)
    else:
        continue
