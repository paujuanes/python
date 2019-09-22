'''
Exercise 9.4

*Solution by Pau Juanes, Sep 22nd 2019*
'''

file_r = open(r'UMichigan_PyCourse\mbox-short.txt')

dct = {}

for line in file_r:
    words = line.split()
    if len(words)>=2 and words[0] == 'From':
        dct[words[1]] = dct.get(words[1], 0) + 1

max_msg = None
max_mail = None

for mail, msg in dct.items():
    if max_mail == None or msg > max_msg:
        max_mail = mail
        max_msg = msg

print(max_mail, max_msg)