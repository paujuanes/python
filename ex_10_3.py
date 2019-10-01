'''
Exercise 10.3

*Solution by Pau Juanes, Sep 30th 2019*
'''
import string

file_r = open(r'UMichigan_PyCourse\romeo-full.txt')

letter_counts = dict()
lettercount = 0

for line in file_r:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
            lettercount += 1

maxletter = list()

for key, val in letter_counts.items():
    maxletter.append((val, key))

maxletter.sort(reverse=True)

for val, key in maxletter[:10]:
    val = round((val/lettercount)*100, 2)
    print(f'Letter {key} represents {val}%')
print(f'For a total of {lettercount} letters in the given text.')