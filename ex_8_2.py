'''
Solution by Pau Juanes Sep 12th 2019
'''

fhand = open(r'ex_8_2.txt')
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])