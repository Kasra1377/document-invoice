# import essential libraries
from collections import namedtuple
import mysql.connector
import pytesseract
import record
import cv2
import os

# in order to use the Pytesseract program, we have to download the application
# and after installing it, we have to pass the installation path into variable
# down below
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

# define a function that recognize and delete non-ASCII
# words that are presented in the form
def cleanup_text(text):
    return "".join([c if ord(c) < 128 else "" for c in text]).strip()

def documentOCR(img, file_name):

    OCRLocation = namedtuple("OCRLocation", ["id", "bbox", "filter_keywords"])

    OCRLOCATIONS = [
    OCRLocation("name", (280, 1600, 705, 110),
    ["Name", "name"]),
    OCRLocation("last_name", (1035, 1600, 700, 120),
    ["last", "name", "last name"]),
    OCRLocation("gender", (1765, 1600, 695, 120),
    ["gender"]),
    OCRLocation("email", (280, 1920, 2190, 110),
    ["email", "address", "email address"]),
    OCRLocation("city", (280, 2200, 705, 110),
    ["city"]),
    OCRLocation("state", (1035, 2200, 705, 110),
    ["state", "state."]),
    OCRLocation("zip_code", (1780, 2200, 690, 110),
    ["zip code", "zip_code", "zipcode"]),
    
    ]

    parsingResults = []

    for loc in OCRLOCATIONS:
        (x, y, w, h) = loc.bbox
        roi = img[y:y + h, x:x + w]

        # rgb = cv2.cvtColor(roi, cv2.COLOR_GRAY2RGB)
        text = pytesseract.image_to_string(roi)

        for line in text.split("\n"):
            # if the input is not specified then pass the N/A
            # value in that specific input field
            if len(line) == 0:
                parsingResults.append((loc , "N/A"))
                
            lower = line.lower()
            count = sum([lower.count(x) for x in loc.filter_keywords])

            if count == 0:
                parsingResults.append((loc , line))

    results = {}
    for (loc, line) in parsingResults:
        r = results.get(loc.id, None)

        if r is None:
            results[loc.id] = (line, loc._asdict())
        else:
            
            (existingText, loc) = r
            text = "{}\n{}".format(existingText, line)
            results[loc["id"]] = (text, loc)
    
    instance = {}
    
    for (locID, result) in results.items():
        (text, loc) = result

        (x, y, w, h) = loc["bbox"]
        clean = cleanup_text(text)

        cv2.rectangle(img, (x, y) , (x + w , y + h), (0, 255, 0), 2)
        for line in clean.split("\n"):

            instance[locID] =  line
            cv2.putText(img, line, (x, y),
                cv2.FONT_HERSHEY_SIMPLEX, 2 , (0, 0, 255), 4)
    # print(instance) 

    OUTPUT_DIR = "ocr-output"

    basename = file_name
    cv2.imwrite(OUTPUT_DIR + "/" + basename,  img)
    print("Successfully OCR'ed " + basename)

    # insert the input infos into database
    record.insert_table(instance)

