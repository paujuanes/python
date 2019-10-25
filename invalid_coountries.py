file_r = open(r'countries.txt', 'r')
file_w = open(r'invalid_countries.txt', 'w')

for line in file_r:
    line = line.rstrip()
    line = '[I]' + line
    file_w.write(line + '\n')
    print(line)

file_r.close()
file_w.close()