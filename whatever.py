import re, string

file_r = open(r'UMichigan_PyCourse\romeo-full.txt')

for line in file_r:
    line = line.rstrip()
    line = line.lower()
    line = line.translate(line.maketrans('', '', string.punctuation))
    if re.search(r'\ba', line):
        words = re.findall(r'\ba\S*i\S*', line)
        print(words)