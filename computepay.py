def computepay(hs, rt):
    if hs <= 40.0 :
        pay = hs * rt
    else:
        pay = (40 * rt) + (hs - 40) * rt * 1.5
    
    return pay
    
"""repeat = input('Do you want to calculate again? (y/n)\n')
if repeat == 'y':
    computepay()
else:
    print('OK, see you again!')
    quit()"""

hours = input("Enter the number of hours:\n")
rate = input("Enter the rate:\n")

try:
    h = float(hours)
    r = float(rate)
except:
    print('Please, enter a valid numeric input.')

p = computepay(h, r)

print('Pay', p)