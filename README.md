# document-invoice

### 📝Description
---
In this repostory, we are going to implement a very interesting project that is called `Document Invoice`. The main appliction of this API is reading a document and insert its information into a database. This process can be done automatically without human interference.Just take a photo from the form in a appropriate position, pass it into a program and thats it; all of the informations have been passed into the database. 

This application contains three main sections: The first one image scanning. To do this, we have to create an API to get an input form, then applies some image preprocessing and then output the scanned image with **high resolution quality**. We want high resolution because the output of Optical Character Recognition (OCR) application which is `pytesseract` is highly dependent on the input image quality.  
