n = float(input('Type the number you want the table of: '))
n = int(n)
for x in range(11):
    if x == 10:
        print(n, 'x', x, '=', n * x)
    else:
        print(n, 'x', x, ' =', n * x)