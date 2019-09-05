def front_back(str):
    lst = list(str)
    lst[0], lst[-1] = lst[-1], lst[0]
    str = ''.join(lst)
    return str

print(front_back('mallek'))
try:
    print(front_back(''))
except:
    print('Please, no empty strings.')
print(front_back('a'))