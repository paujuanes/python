f_read = open(r'UMichigan_PyCourse\mbox-short.txt')

for line in f_read :
    line = line.rstrip()
    print(line.upper())

f_read.close()