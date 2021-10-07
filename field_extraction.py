import cv2
import os

image_path = "output/sample2.jpg"
img = cv2.imread(image_path)

# draw a rectangle on each and every field to 
# show what we are interested to exract 
cv2.rectangle(img, (280, 1620), (985, 1720), (0, 255 ,0),3)    # name
cv2.rectangle(img, (1035, 1610), (1735, 1720), (0, 255 ,0),3)   # last name
cv2.rectangle(img, (1765, 1610), (2460, 1720), (0, 255 ,0),3)   # gender
cv2.rectangle(img, (280, 1920), (2470, 2020), (0, 255 ,0),3)    # email
cv2.rectangle(img, (280, 2220), (985, 2310), (0, 255 ,0),3)    # city
cv2.rectangle(img, (1035, 2200), (1740, 2310), (0, 255 ,0),3)   # state
cv2.rectangle(img, (1780, 2210), (2470, 2310), (0, 255 ,0),3)   # zipcode
cv2.rectangle(img, (260, 2450), (2460, 2920), (0, 255 ,0),3)    # signature


OUTPUT_DIR = "extractions"
basename = os.path.basename(image_path)
cv2.imwrite(OUTPUT_DIR + "/" + basename,  img)
print("Successfully extracted " + basename)
