'''
We want to make a row of bricks that is goal centimeters long.
We have a number of small bricks (1 cm each) and big bricks (5 cm each).
Return True if it is possible to make the goal by choosing from the given bricks.
This is a little harder than it looks and can be done without any loops.

* Solution by Pau Juanes, Oct 4th 2019 *
'''

def make_bricks(small, big, goal):
    if (small + (5*big)) < goal:  # not enough cm, nope
        return False
    else:
        if (small + (5*big)) % goal == 0:  # exact amount of cm, yep
            return True
        elif small >= goal % 5 and (5*big + small) > goal:  # enough small and big bricks, yep
            return True
        return False