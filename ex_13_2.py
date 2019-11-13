'''
Exercise 13.2 (Assignment)
Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py.
The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract
the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below.

*Solution by Pau Juanes, Nov 10th 2019*
'''

import urllib.request
import json

url = input('Enter location: ')
print(f'Retrieving {url}')
data = urllib.request.urlopen(url).read().decode()

js = json.loads(data)

#print(f'Retrieved data:\n {json.dumps(js, indent=4)}')
print(f'Retrieved {len(data)} characters')

users = js['comments']
comments = [user['count'] for user in users]

print(f'Count: {len(comments)}')
print(f'Sum: {sum(comments)}')