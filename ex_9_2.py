'''
Exercise 9.2

*Solution by Pau Juanes, Sep 21st 2019*
'''

file_r = open(r'UMichigan_PyCourse\mbox-short.txt')

dct = {}

for line in file_r:
    words = line.split()
    if len(words)>=3 and words[0] == 'From':
        dct[words[2]] = dct.get(words[2], 0) + 1

print(dct)