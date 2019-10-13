'''
Exercise 11.1
Write a simple program to simulate the operation of the grep command on Unix.
Ask the user to enter a regular expression and count the number of lines
that matched the regular expression.

*Solution by Pau Juanes, Oct 13th 2019*
'''
import re

file = input('Enter the name of the file: ')
regexp = input('Enter a regular expression: ')
file_r = open(file)

countLines = 0  # Counting lines that match
totLines = 0    # Counting all lines

for line in file_r:
    totLines += 1
    line = line.rstrip()
    if re.search(regexp, line):
        countLines += 1

percent = round(countLines/totLines*100, 2)
print(f'{file} had {countLines}/{totLines}({percent}%) lines that matched {regexp}')