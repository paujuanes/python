'''
Exercise 9.3

*Solution by Pau Juanes, Sep 22nd 2019*
'''

file_r = open(r'UMichigan_PyCourse\mbox-short.txt')

dct = {}

for line in file_r:
    words = line.split()
    if len(words)>=2 and words[0] == 'From':
        dct[words[1]] = dct.get(words[1], 0) + 1

print(dct)