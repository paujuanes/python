'''
Exercise 12.3 (Assignment)
Following Links in Python

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py.
The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract
the comment counts from the XML data, compute the sum of the numbers in the file.

*Solution by Pau Juanes, Nov 6th 2019*
'''

import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')

data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)

comments = tree.findall('comments/comment')
counts = []

for comment in comments:
    counts.append(int(comment.find('count').text))

print(sum(counts))