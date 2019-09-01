"""
year = int(input('Type a year:\n'))

if type(year) != int:
    print('Please, enter a numerical year.')

year = None
"""

def leapYear():
    year = int(input('Enter a year:\n'))
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print(year, 'IS a leap year!')
            else:
                print(year, 'is NOT a leap year.')
        else:
            print(year, 'IS a leap year!')
    else:
        print(year, 'is NOT a leap year.')

    repeat = str(input('Do you you want to try again? (y/n)\n'))

    if repeat == 'y':
        leapYear()
    else:
        print('OK, see you soon!')

leapYear()