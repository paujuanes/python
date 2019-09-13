'''
Exercise 8.5

*Solution by Pau Juanes, Sep 13th 2019*
'''

file_r = open(r'UMichigan_PyCourse\mbox-short.txt')

count = 0

for line in file_r:
    words = line.split()                       # Split the line into words
    if len(words) < 2 or words[0] != 'From':   # If the line is less than 2 words long or
        continue                               # the first word is not 'From', ignore it
    print(words[1])                            # Otherwise, print the second word (email)
    count += 1                                 # Update the counter

print('There were {} lines in the file with From as the first word.'.format(count))