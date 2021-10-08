# document-invoice

### 📝Description
---
In this repostory, we are going to implement a very interesting project that is called `Document Invoice`. The main appliction of this API is reading a document and insert its information into a database. This process can be done automatically without human interference.Just take a photo from the form in a appropriate position, pass it into a program and thats it; all of the informations have been passed into the database. 

This application contains three main sections: The first one image scanning. To do this, we have to create an API to get an input form, then applies some image preprocessing and then output the scanned image with **high resolution quality**. We want high resolution input because the output accuracy of Optical Character Recognition (OCR) application which is `pytesseract` is highly dependent on the input image quality.  

The second section is to define the OCR funcion to grab the preprocessed form and extract each and every information from prespecified locations. And the last step is to create a sql database and connect it to the Python file.

We will be going through into each these subcategories more deeply in the next section.

### 🖥 Installation
---
The Code is written in Python 3.7.5. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensure you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after cloning the repository:
```
git clone git@github.com:Kasra1377/lbp-face-recognition.git
```
or
```
git clone https://github.com/Kasra1377/lbp-face-recognition.git
```
After you cloned this repository, you have to download and install the Anaconda. You can find the download link from this [link](https://www.anaconda.com/products/individual). After the installation, open the Anaconda Prompt and type the code down below:
```
conda create -n verification python=3.7
```
This command creates a virtual env with a name of `verification`. Note that you can choose your own arbitrary name for virtual enviroment. After virtual enviroment is created,  switch to the directory of the project folder via Anaconda Prompt and then type:

```
conda activate verification
```
This command activates your own virtual enviroment that you have just created. In order to install all of the libraries that used in this project, you have to type:

```
conda install file requirements.txt
```

By doing this and downloading all of the required packages, you are ready to run this project on your local computer.

### 🛠Project Structure
---

#### Image Scanning
This is the most important step in this project. Because it contains image preprocessing step and without appropriate preprocessing we are not able to get appropriate results. Our image preprocessing steps contains of: `contour detection`, `morphological operations` and `image sharpening`. Thanks to this [repository](https://github.com/andrewdcampbell/OpenCV-Document-Scanner) most of the programming steps is done.

To start by, first the input image is passed into program, then [lsd](https://github.com/primetang/pylsd) module detects the boundary lines in the image. Then boundaries will be divided into horizontal

#### OCR'ing The Scanned Image
The next important step is to read the document fields. To do so,we use `Pytesseract` program to reach our purpose. You can download the Pytesseract installer via this [link](https://github.com/UB-Mannheim/tesseract/wiki). In order to complete this task, we defined two functions; `clearup_text` to omit words that OCR can not read them and `documentOCR`. In this function we utilized `namedtuples` for grouping objects without defining a class. This is one of the important feartures that Python has.

> namedtuples are immutable containers, just like regular
tuples. Once you store data in top-level attribute on a namedtuple,
you can’t modify it by updating the attribute. All attributes on a
namedtuple object follow the “write once, read many” principle.
Each object stored in them can be accessed through a unique (human-readable)
identifier. This frees you from having to remember integer indexes,
or resorting to workarounds like defining integer constants as
mnemonics for your indexes.

--- Page 130, [Python Tricks The Book A Buffet of Awesome Python Features](https://www.amazon.com/Python-Tricks-Buffet-Awesome-Features/dp/1775093301)

To create a namedtuple, we have to define a `typename` and define a name for each field and put the names into a list and pass it into `namedtyple` API. The fields are: `id` which is the ID of each fields in the form, `bbox` which is the bounding box points for each field and the last one is `filter-keywords` which is the words that we filter in order to OCR do not recognize them as inputs. The words of this section mostly contains of field names such as Name, Last Name, etc.

#### Database Connection
The last step is the connection between SQL database and Python files. In this specific project I selected MySQL platform and in order to run this project on your local computer you have to download MySQL from this [link](https://dev.mysql.com/downloads/workbench/). In addition `my-sql.connector` library must be installed on your computer. In order to install it, open up your Command Prompt and type

```
pip install mysql-connector-pytho
```
Or you can type the below command if you want to install this library in Anaconda Prompt:

```
conda install -c anaconda mysql-connector-python
```
After the installation, open up MySQL program and and create a Connection. Give it a name and a `password` and set the `user` to `root`, after that create a database:

```sql
CREATE DATABASE documents;
```
and select this database

```sql
USE documents;
```
after that create a table with a name of `documents`:

```sql
CREATE TABLE documents (
name VARCHAR(30),
last_name VARCHAR(50),
gender VARCHAR(6),
email VARCHAR(50),
city VARCHAR(30),
state VARCHAR(30),
zip_code VARCHAR(12),
)
```

now go to the `record.py` file and change the password section of below script:

```python
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="your password",
    database="documents",
)

```
After doing this, the installation is done and you are ready to run the project on your local computer. Please take note that, you have to run the `main.py` python file in order to automate all of the process.


