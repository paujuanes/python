'''
Given 3 int values, a b c, return their sum.
However, if any of the values is a teen -- in the range 13..19 inclusive --
then that value counts as 0, except 15 and 16 do not count as a teens.
Write a separate helper "def fix_teen(n):" that takes in an int value and returns
that value fixed for the teen rule.

* Solution by Pau Juanes, Oct 5th 2019 *
'''

teens = (13, 14, 17, 18, 19)
def fixTeen(n):
    if n in teens: return 0
    return n
def noTeenSum(a, b, c):
    if a in teens or b in teens or c in teens:
        return fixTeen(a) + fixTeen(b) + fixTeen(c)
    return a + b + c

'''
def noTeenSum(a, b, c):
    teens = (13, 14, 17, 18, 19)
    if a in teens and b in teens and c in teens: return 0
    elif a not in teens and b not in teens and c not in teens: return a + b + c
    else:
        if a in teens:
            if b in teens: return c
            elif c in teens: return b
            return b + c
        elif b in teens:
            if c in teens: return a
            return a + c
        else: return a + b
'''