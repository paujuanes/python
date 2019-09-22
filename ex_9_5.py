'''
Exercise 9.5

*Solution by Pau Juanes, Sep 22nd 2019*
'''

file_r = open(r'UMichigan_PyCourse\mbox-short.txt')

dct = {}

for line in file_r:
    words = line.split()
    if len(words)>=2 and words[0] == 'From':      # Only look for 'From' lines
        email = words[1].partition('@')           # Split the email at '@'
        dct[email[2]] = dct.get(email[2], 0) + 1  # Add the domain to the dict

print(dct)