'''
Exercise 11.3 (Assignment)
Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers.
You will extract all the numbers in the file and compute the sum of the numbers.

*Solution by Pau Juanes, Oct 13th 2019*
'''

import re

file_r = open('regex_sum_273033.txt')
numList = list()

for line in file_r:
    line = line.rstrip()
    if re.search(r'\d+', line):
        lst = re.findall(r'\d+', line)
        for num in lst:
            numList.append(int(num))

print(sum(numList))