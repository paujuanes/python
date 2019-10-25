import re, string, collections

file_r = open(r'txt\bible.txt')

lst = list()

for line in file_r:
    line = line.rstrip()
    line = line.lower()
    line = line.translate(line.maketrans('', '', string.punctuation))
    if re.search(r'(\bh\S+)\s', line):
        words = re.findall(r'(\bh\S+)\s', line)
        for word in words:
            lst.append(word)
        #print(word)

#print(lst)

c = collections.Counter(lst)
top = c.most_common(20)

for k,v in top:
    print(k,v)