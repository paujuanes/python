'''
For this problem, we'll round an int value up to the next multiple of 10
if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately,
round down to the previous multiple of 10 if its rightmost digit is less
than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of
their rounded values.

* Solution by Pau Juanes, Oct 5th 2019 *
'''

def round10(n):
    if n % 10 >= 5: return n + 10 - (n % 10)
    return n - n % 10
def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)