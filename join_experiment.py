def join(iterable, char):
    if type(iterable) == str:
        lst = list()
        for i in range(len(iterable)):
            if i == len(iterable)-1:
                newchar = iterable[i]
            else:
                newchar = iterable[i] + char
            lst.append(newchar)
        return ''.join(lst)
    elif type(iterable) == list:
        for i in range(len(iterable)-1):
            string = iterable[i] + char
        return string

strn = 'parallel'
st = '-'.join(strn)
print('With join method:', st)

st2 = join(strn, '-')
print(strn)
print('With my join:', st2)