# from asyncore import file_dispatcher
import PyPDF2
import re
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
# root.withdraw()
file_path1 = filedialog.askopenfilename()
# file_path2 = filedialog.askopenfilename()
root.withdraw()
if(file_path1.endswith('.pdf')) :#and file_path2.endswith('.pdf')):
    a = PyPDF2.PdfFileReader(file_path1)
f = """Now a days you can learn almost anything by just visiting http://www.google.com. But if you are completely new to computers or internet then first you need to leanr those fundamentals. Next
you can visit a good e-learning site like - https://www.tutorialspoint.com to learn further on a variety of subjects."""
# with open("web.txt") as file:
for line in file_path1 :  
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
    print(urls)

