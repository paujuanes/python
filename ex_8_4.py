'''
Exercise 8.4

*Solution by Pau Juanes, Sep 13th 2019*
'''

file_r = open(r'UMichigan_PyCourse\romeo.txt')

wordlist = []

for line in file_r:
    words = line.split()                # Splits the line into words
    for word in words:
        if word in wordlist: continue   # Ignores repeated words
        wordlist.append(word)           # Adds new words to the list

wordlist.sort()                         # Sorts the list alphabetically
print(wordlist)