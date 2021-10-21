#audiobook
import os
import PyPDF2
from win32com.client import Dispatch
pdf = r"C:\Users\HP\Desktop\Books"
list = os.listdir(pdf)
print(list)
book = r"C:\Users\HP\Desktop\Books\who where the shudras.pdf"
read = PyPDF2.PdfFileReader(book)
no = read.getNumPages()
print(f" No of pages in book : {no}")
print(f" Info of book : {read.documentInfo}")
str = ""
for i in range(10,12):
    str += read.getPage(i).extractText()
    speak = Dispatch('SAPI.SpVoice')
    speak.speak(str)
print(str)