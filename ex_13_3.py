'''
Exercise 13.3 (Assignment)
Calling a JSON API

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py.
The program will prompt for a location, contact a web service and retrieve JSON for the web service,
parse that data and retrieve the first place_id from the JSON. A place ID is a textual identifier that
uniquely identifies a place as within Google Maps.

*Solution by Pau Juanes, Nov 13th 2019*
'''

import urllib.request, urllib.parse
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'
api_key = 42

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    
    parms = dict()
    parms['address'] = address
    parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print(f'Retrieving {url}')
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    js = json.loads(data)
    print(f'Retrieved {len(data)} characters')
    #print(json.dumps(js['results'], indent=4))

    print(f"Place id {js['results'][0]['place_id']}")
