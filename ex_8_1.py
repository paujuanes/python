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