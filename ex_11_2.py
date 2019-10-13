'''
Exercise 11.2
Write a program to look for lines of the form `New Revision: 39772`
and extract the number from each of the lines using a regular expression
and the findall() method. Compute the average of the numbers and print out
the average.

*Solution by Pau Juanes, Oct 13th 2019*
'''
import re

file = input('Enter file: ')
file_r = open(file)
lst = list()  # A list to store the values
counts = 0    # Counting the numbers found

for line in file_r:
    line = line.rstrip()
    if re.search('^New .*: \d+', line):
        num = re.findall('^New .*: (\d+)', line)[0]  # Finding and storing the number
        lst.append(int(num))  # Appending the number to the list as an int
        counts += 1

avg = sum(lst)/counts  # Calculating the average with a list sum
print(avg)