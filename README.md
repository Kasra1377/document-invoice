# document-invoice

### 📝Description
---
In this repostory, we are going to implement a very interesting project that is called `Document Invoice`. The main appliction of this API is reading a document and insert its information into a database. This process can be done automatically without human interference.Just take a photo from the form in a appropriate position, pass it into a program and thats it; all of the informations have been passed into the database. 

This application contains three main sections: The first one image scanning. To do this, we have to create an API to get an input form, then applies some image preprocessing and then output the scanned image with **high resolution quality**. We want high resolution input because the output accuracy of Optical Character Recognition (OCR) application which is `pytesseract` is highly dependent on the input image quality.  

The second section is to define the OCR funcion to grab the preprocessed form and extract each and every information from prespecified locations. And the last step is to create a sql database and connect it to the Python file.

We will be going through into each these subcategories more deeply in the next section.

### 🛠Project Structure
---

#### Image Scanning
This is the most important step in this project. Because it contains image preprocessing step and without appropriate preprocessing we are not able to get appropriate results. Our image preprocessing steps contains of: `contour detection`, `morphological operations` and `image sharpening`. Thanks to this [repository](https://github.com/andrewdcampbell/OpenCV-Document-Scanner) most of the programming steps is done.

To start by, first the input image is passed into program, then [lsd](https://github.com/primetang/pylsd) module detects the boundary lines in the image. Then boundaries will be divided into horizontal
