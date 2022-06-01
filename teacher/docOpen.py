#!C:/python/python
print("<h1>Plagiarism Detection</h1>")
from wsgiref import headers
import tkinter as tk
from tkinter import filedialog
# import docx
from googlesearch import search 
import docx2txt
# from docx import *
root = tk.Tk()
# root.withdraw()
file_path1 = filedialog.askopenfilename()
file_path2 = filedialog.askopenfilename()
root.withdraw()
# document = opendocx(file_path1)
with open(file_path1) as file1,open(file_path2) as file2:
    text1 = docx2txt.process(file_path1)
    text2 = docx2txt.process(file_path2)
# print(text1)
# print(text2)
print("First File:--> ",file_path1)
print("<br/>")
print("Second File:--> ",file_path2)
print("<hr/>")
a = text1.split()
b = text2.split()
l1 = len(a)
l2 = len(b)
c = []
for i in a:
    if i in b:
        c.append(i)
l3 = len(c)
# print("Common words from both file : --> ",c)
# print("<hr/>")
# print("length of first file's words: ",l1)
# print("<br/>")
# print("length of second file's words: ",l2)
# print("<br/>")
# print("length of Common words: ",l3)
# print("<br/>")
#print("length of first file: ",l3)
total_legth = l1+l2
aveg = 2.0*l3/total_legth*100
sim = round(aveg,2)
print("""<tr bgcolor="#c7cfd1">
              	<td colspan="2" align="center">
                  <table width="100%">
    <tr bgcolor="#c7cfd1">
    <th>First File</th>
    <th>Second File</th>
    <th>Common words from both file</th>
  </tr>
  <tr>
    <td align="center" bgcolor="#759ebe"> {} <br/><br/><br/><b>length of words: <b/>{} </td>
    <td align="center" bgcolor="#759ebe"> {} <br/><br/><br/><b>length of words: <b/>{} </td>
    <td align="center" bgcolor="#759ebe"> {} <br/><br/><br/><b>length of words: <b/>{} </td>
  </tr>
  
</table>""".format(a,l1,b,l2,c,l3))
print("<h2><br/><br/><b>Content Similarity Report:<br/> Similarity {}% Match found<b/></h2>".format(sim))

print("<h2>Plagiarism Report:</h2><br/>")
print("1st File's content referse from:-->")
for url in search(text1,stop=5):
  print("""<p style="color:red;">{}</p>""".format(url))
  # print(url,"<br/>")
print("<br/>")
print("2nd File's content referse from:-->")
for url in search(text2,stop=5):
  print("""<p style="color:red;">{}</p>""".format(url))

root.withdraw()
