import PyPDF2
from tabulate import tabulate
# print(a.documentInfo)
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
file_path1 = filedialog.askopenfilename()
file_path2 = filedialog.askopenfilename()
if(file_path1.endswith('.pdf') and file_path2.endswith('.pdf')):
    a = PyPDF2.PdfFileReader(file_path1)
    b = PyPDF2.PdfFileReader(file_path1)
    print(file_path1)
    print(file_path2)
    # print(tabulate(a, headers=("file1","file2")))
    # print(a.documentInfo)
    pg1 = a.getNumPages()
    pg2 = b.getNumPages()
    print(pg1)
    print(pg2)
    str1 = ""
    str2 = ""
    common = []
    for i in range(0,pg1):
        str1 += a.getPage(i).extractText()
    # print(str)
    for j in range(0,pg2):
        str2 += b.getPage(j).extractText()
    s1 = str1.split()
    s2 = str2.split()
    for c in s1:
        if c in s2:
            common.append(c)
    print("common string is: ",common)
    ll1 = len(s1)
    ll2 = len(s2)
    ll3 = len(common)
    print("length of first file string is : ",ll1)
    print("length of second file string is : ",ll2)
    print("length of common string is : ",ll3)
    tt = ll1+ll2
    plg = 2.0*ll3/tt*100
    print(round(plg,2),"%Macth")
else:
    print(file_path1)
    print(file_path2)
    with open(file_path1) as file1, open(file_path2) as file2:#,open('file3.txt') as file3:
        file1_data = file1.read()
        file2_data = file2.read()
 #   file3_data = file3.read()
    a = file1_data.split()
    b = file2_data.split()
    l1 = len(a)
    l2 = len(b)
    c = []
    for i in a:
        if i in b:
            c.append(i)
    l3 = len(c)
    print("Common words from both file : --> ",c)
    print("<hr/>")
    print("length of first file's words: ",l1)
    print("<hr/>")
    print("length of second file's words: ",l2)
    print("<hr/>")
    print("length of Common words: ",l3)
    print("<hr/>")
    #print("length of first file: ",l3)
    total_legth = l1+l2
    aveg = 2.0*l3/total_legth*100
    print(round(aveg,2),"%Macth")
input('press any key to exit')
