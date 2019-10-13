'''
We want to make a package of goal kilos of chocolate.
We have small bars (1 kilo each) and big bars (5 kilos each).
Return the number of small bars to use, assuming we always use big bars before small bars.
Return -1 if it can't be done.

* Solution by Pau Juanes, Oct 4th 2019 *
'''

def make_chocolate(small, big, goal):
    if (small + (5*big)) < goal:  # not enough kg, nope
        return -1
    else:
        if 5*big > goal:  # 
            if goal % 5 == 0:
                return 0
            elif small < goal % 5:
                return -1
            elif small >= goal % 5:
              return goal % 5
        elif goal > 5*big:
            return goal - 5*big
        else:
            return goal % 5

print(make_chocolate(4, 1, 4))
print(make_chocolate(4, 1, 9))
print(make_chocolate(4, 1, 7))
print(make_chocolate(9, 3, 18))
print(make_chocolate(1, 2, 6))