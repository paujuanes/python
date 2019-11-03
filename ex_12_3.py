'''
Exercise 12.3 (Assignment)
Following Links in Python

In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py.
The program will use urllib to read the HTML from the data files below, extract the href= values from
the anchor tags, scan for a tag that is in a particular position relative to the first name in the list,
follow that link and repeat the process a number of times and report the last name you find.

*Solution by Pau Juanes, Nov 2nd 2019*
'''

from bs4 import BeautifulSoup as BS
import urllib.request
import re

url = input('Enter URL: ')
pos = int(input('Enter position: '))
repeat = int(input('Enter count: '))
firstName = re.findall(r'_by_(\w+).html', url)
seqNames = [firstName[0]]

while repeat > 0:
    file_r = urllib.request.urlopen(url).read()
    content = BS(file_r, 'html.parser')
    tags = content('a')
    strTags = [str(tag) for tag in tags]
    data = re.findall(r'^<a href="(http[s]?://.+\.html)">(\w+)<', strTags[pos-1])
    url = data[0][0]
    name = data[0][1]
    print('Retrieving: ', url)
    seqNames.append(name)
    repeat -=1

print('Sequence of names: ', ' '.join(seqNames))
print('Last name in sequence: ', name)