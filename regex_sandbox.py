import re, string, collections

file_r = open(r'txt\bible.txt')

lst = list()

for line in file_r:
    line = line.rstrip()
    line = line.lower()
    line = line.translate(line.maketrans('', '', string.punctuation))
    if re.search(r'(\bl\S{3})\s', line):
        words = re.findall(r'(\bl\S{3})\s', line)
        for word in words:
            lst.append(word)
        #print(word)

#print(lst)

c = collections.Counter(lst)
common = c.most_common(10)

print(common)