'''
Exercise  8.1: Write a function called chop that takes a list and modifies it,
removing the first and last elements, and returns None.

Then write a function called middle that takes a list and returns a new list
that contains all but the first and last e lements.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Pau Juanes, Sep 12th 2019
'''

def chop(lst):
    del lst[0]
    del lst[-1]

def middle(lst):
    new_lst = lst [1:-1]
    return new_lst

lst = [1, 2, 3, 4, 5]
lst2 = [1, 2, 3, 4, 5]

print('- - - chop function: - - -'.center(34, '·') + '\n')
print('Takes this list:', lst)
print('Returns', chop(lst))
print('And modifies the list:', lst)
print('\n')
print('- - - middle function: - - -'.center(34, '|') + '\n')
print('Takes this list:', lst2)
print('Returns a new one:', middle(lst2))
print('And leaves the original unchanged:', lst2)