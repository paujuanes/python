hrs = input('Enter Hours:\n')
try:
    h = float(hrs)
except:
    h = -1

rate = input('Enter Rate:\n')
try:
    r = float(rate)
except:
    r = -1

if r<0:
    print('Please, enter a valid rate.')

if h>=0 and h<=40:
    pay = h * r
    print(pay)

elif h>40:
    pay = (40 * r) + ((h-40) * r * 1.5)
    print(pay)

else:
    print('Please, enter a valid number for hours.')