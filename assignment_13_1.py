#Extracting Data from XML

#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py.
#The program will prompt for a URL, read the XML data from that URL using urllib and then parse
#and extract the comment counts from the XML data, compute the sum of the numbers in the file.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_38798.xml (Sum ends with 55)

#<comment>
  #<name>Matthias</name>
  #<count>97</count>
#</comment>
#You are to look through all the <comment> tags and find the <count> values sum the numbers.
#The closest sample code that shows how to parse XML is geoxml.py.
#But since the nesting of the elements in our data is different than the data we are parsing
#in that sample code you will have to make real changes to the code.
#To make the code a little simpler, you can use an XPath selector string to
#look through the entire tree of XML for any tag named 'count' with the following line of code:

#counts = tree.findall('.//count')
#Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details.
#You could also work from the top of the XML down to the comments node and then loop through the child nodes of the comments node.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter - ')
print('1_Retrieving', url, type(url)) #class str
uh = urllib.request.urlopen(url)
print('2_uh', uh, type(uh)) #class 'http.client.HTTPResponse'
data = uh.read()
print("3_uh.read() or data", data, type(data)) #calss bytes
data = data.decode()
print("4_data decode", data, type(data)) #class str
tree = ET.fromstring(data)
print("5_tree", tree, type(tree)) #class 'xml.etree.ElementTree.Element'
count = tree.findall('.//count')
print("6_count", count, type(count), "len", len(count)) #class 'list
i = 0
i = int(i)
sumnum = list()
while True :
    try :
        countext = count[i].text
        countext = int(countext)
        sumnum.append(countext)
        print("7_count", countext, type(countext))
        i = i + 1
        continue
    except :
        break
print("sumnum", sum(sumnum), type(sumnum))
