#!C:/python/python
print()
from googlesearch import search 
print("<h1>Plagiarism Analyzers</h1>")
from wsgiref import headers
import docx2txt
import PyPDF2
# import nltk
# from nltk.corpus import stopwords
from tabulate import tabulate
# print(a.documentInfo)
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
# root.withdraw()
file_path1 = filedialog.askopenfilename()
file_path2 = filedialog.askopenfilename()
root.withdraw()
stpwords = ('at', 'hadn', 'will', 'its', 'should', 'being', 's', 'i', 'both', "isn't", 'few', 'just', 'him', 'herself', 'who', 'hers', 'do', 'don', 'so', 'mustn', 'too', 'our', "you'd", 'you', 'than', 'a', 'to', 'under', 'been', 'while', 'll', "mightn't", 'that', 'if', 'during', 'was', 'off', 't', 'with', 'these', 'yours', 'their', 'or', 'can', 'only', 'by', 'up', "hasn't", "mustn't", "you've", 'whom', 'where', 'and', 'did', 'it', 
'o', 'they', 'over', "shouldn't", 'we', 'out', 'then', 'again', 'he', 'isn', 'couldn', 'what', "it's", 'into', "don't", 're', 'above', 'no', 'ma', 'below', 'here', 'theirs', 'how', "didn't", 'once', 'all', 'from', 'those', 'until', 'before', 'won', 'most', "needn't", 'them', 'your', "you'll", 'm', 'an', 'itself', 'against', 'ain', 'some', 'further', 'each', 'when', 'doing', 've', 'there', 'because', "doesn't", "wouldn't", 'in', 'not', 'aren', 'down', 'are', 'does', 'any', 'more', 'having', 'the', "shan't", 'now', 'd', 'ours', 'as', 'wasn', 'but', "couldn't", 'her', 'nor', 'which', 'my', "wasn't", 'this', 'between', 'yourself', 'own', 'shouldn', 'weren', 'had', 'very', 'mightn', 'yourselves', 'on', "you're", 'y', "that'll", 'same', 'myself', 'his', "she's", "won't", 'me', 'am', 'for', "should've", 'ourselves', 'have', 'needn', 'she', 'shan', 'himself', 'is', "haven't", 'didn', 'haven', 'other', 'were', "hadn't", 'themselves', 'through', 'doesn', 'hasn', 'wouldn', 'about', 'after', "weren't", 'has', 'of', 'such', 'be', "aren't", 'why')
if(file_path1.endswith('.pdf') and file_path2.endswith('.pdf')):
    a = PyPDF2.PdfFileReader(file_path1)
    b = PyPDF2.PdfFileReader(file_path2)
    print("First file's path: ",file_path1)
    print("<br/>")
    print("Second file's path: ",file_path2)
    # print(tabulate(a, headers=("file1","file2")))
    print("<hr/>")
    # print(a.documentInfo)
    pg1 = a.getNumPages()
    pg2 = b.getNumPages()
    print("Number of pages in (first file): ",pg1)
    print("<br/>")
    print("Number of pages in (Second file file): ",pg2)
    print("<br/>")
    print("<br/>")
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
    print("<h2>Plagiarism Report:</h2><br/>")
    print("1st File's content referse from:-->")
    for url in search(str1,stop=3):
      print("""<p style="color:red;">{}</p>""".format(url))
    # print(url,"<br/>")
    print("<br/>")
    print("2nd File's content referse from:-->")
    for url in search(str2,stop=3):
      print("""<p style="color:red;">{}</p>""".format(url))
    for c in s1:
        if c in s2:
            common.append(c)
    # print("common string is: ",common)
    print("<hr/>")
    ll1 = len(s1)
    ll2 = len(s2)
    ll3 = len(common)
    # print("length of first file string is : ",ll1)
    # print("<br/>")
    # print("length of second file string is : ",ll2)
    # print("<br/>")
    # print("length of common string is : ",ll3)
    # print("<br/>")
    tt = ll1+ll2
    plg = 2.0*ll3/tt*100
    sims = round(plg,2)
    print("""<table>
  <tr bgcolor="#c7cfd1">
    <th>First File</th>
    <th>Second File</th>
    <th>Common words from both file</th>
  </tr>
  <tr>
    <td align="center" bgcolor="#759ebe"> {} <br/><br/><br/><b>length of words: <b/> {} </td>
    <td align="center" bgcolor="#759ebe"> {} <br/><br/><br/><b>length of words: <b/> {} </td>
    <td align="center" bgcolor="#759ebe"> {} <br/><br/><br/><b>length of words: <b/> {} </td>
  </tr>
  
</table>""".format(s1,ll1,s2,ll2,common,ll3))
    print("<h2><br/><b>Content Similarity Report<br/> Similarity {}% Match found<b/>".format(sims))
    print("<br/>")
    print("""
    <button onclick="myFunction()">Generate Report</button>
    <script>
    function myFunction() {
    location.replace("pl_report.html")
    }
    </script>""")

if(file_path1.endswith('.txt') and file_path2.endswith('.txt')):
    print("First File:--> ",file_path1)
    print("<br/>")
    print("Second File:--> ",file_path2)
    print("<hr/>")
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
    siml = round(aveg,1)
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
print("<h2><br/><br/><b>Content Similarity Report:<br/> Similarity {}% Match found<b/></h2>".format(siml))

print("<h2>Plagiarism Report:</h2><br/>")
print("1st File's content referse from:-->")
for url in search(file1_data,stop=3):
  print("""<p style="color:red;">{}</p>""".format(url))
  # print(url,"<br/>")
print("<br/>")
print("2nd File's content referse from:-->")
for url in search(file2_data,stop=3):
  print("""<p style="color:red;">{}</p>""".format(url))
print("<br/>")


  
print("""
<button onclick="myFunction()">Generate Report</button>

<script>
function myFunction() {
  location.replace("pl_report.html")
}
</script>""")


#print("<h2>Redirect to a Webpage</h2>")
#<p>The replace() method replaces the current document with a new one:</p>
# print("""<h1>Plagiarism Analyzer</h1>

# <div id="piechart"></div>

# <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>

# <script type="text/javascript">
# var cv = 8;
# // Load google charts
# google.charts.load('current', {'packages':['corechart']});
# google.charts.setOnLoadCallback(drawChart);

# // Draw the chart and set the chart values
# function drawChart() {
 
#   var data = google.visualization.arrayToDataTable([
#   ['Task', 'Hours per Day'],
#   ['Copied Content', cv],
#   ['Unique Content', 2]
# ]);

#   // Optional; add a title and set the width and height of the chart
#   var options = {'title':'Plagiarism Report:', 'width':550, 'height':400};

#   // Display the chart inside the <div> element with id="piechart"
#   var chart = new google.visualization.PieChart(document.getElementById('piechart'));
#   chart.draw(data, options);
# }
# </script>""")

root.withdraw()