'''
Exercise 10.2

*Solution by Pau Juanes, Sep 29th 2019*
'''

file_r = open(r'UMichigan_PyCourse\mbox-short.txt')

time_counts = dict()

for line in file_r:
    words = line.split()
    if len(words) >= 6 and words[0] == 'From':
        time = words[-2].split(':')
        time_counts[time[0]] = time_counts.get(time[0], 0) + 1

''' Long version:
maxtime = list()

for key, val in time_counts.items():
    maxtime.append((key, val))

maxtime.sort()
'''

maxtime = sorted(list(time_counts.items()))  # Short version
for key, val in maxtime:
    print(key, val)