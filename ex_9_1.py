'''
Exercise 9.1

*Solution by Pau Juanes, Sep 15th 2019*
'''

file_r = open(r'UMichigan_PyCourse\words.txt')

dct = {}

for line in file_r:
    words = line.split()
    for word in words:
        word = word.lower()            # Convert to lowercase to avoid duplicates
        dct[word] = dct.get(word, 0)   # Values don't matter, so 0 is a good default value

print('python' in dct.keys())
print('book' in dct.keys())