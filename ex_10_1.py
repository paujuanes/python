'''
Exercise 10.1

*Solution by Pau Juanes, Sep 29th 2019*
'''

file_r = open(r'UMichigan_PyCourse\mbox.txt')

counts = dict()

for line in file_r:
    words = line.split()
    if len(words) >= 1 and words[0] == 'From':
        counts[words[1]] = counts.get(words[1], 0) + 1

maxcommits = list()
for key, val in counts.items():
    maxcommits.append((val, key))

maxcommits.sort(reverse=True)

print(maxcommits[0][1], maxcommits[0][0])