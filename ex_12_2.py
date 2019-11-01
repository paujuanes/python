'''
Exercise 12.2 (Assignment)
Scraping Numbers from HTML using BeautifulSoup

In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py.
The program will use urllib to read the HTML from a data file and parse the data,
extracting numbers and computing the sum of the numbers in the file.

*Solution by Pau Juanes, Nov 1st 2019*
'''

from bs4 import BeautifulSoup as BS
import urllib.request
import re

url = input('Enter - ')

file_r = urllib.request.urlopen(url).read()
content = BS(file_r, 'html.parser')
tags = content('span')

numbers = [int((re.findall(r'>(\d+)<', str(tag)))[0]) for tag in tags]

# Different method: joining the BeautifulSoup list in
# one string and finding the numbers in that list 
#strn = ''.join(str(tags))
#str_numbers = re.findall(r'nts">(\d+)</span', strn)
#numbers = map(int, str_numbers)

print('Count', len(numbers))
print('Sum', sum(numbers))