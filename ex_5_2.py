maxim = None
minim = None
count = 0

while True:
    inp = input('Enter a number:\n')
    if count == 0 and inp == 'done':
        print('Please, enter at least one number.')
        continue
    elif count != 0 and inp == 'done':
        break
    else:
        try:
            num = int(inp)
            count += 1
            if count == 1 :
                maxim = num
                minim = num
            if maxim is None or num > maxim :
                maxim = num
                continue
            elif minim is None or num < minim :
                minim = num
                continue
        except:
            print('Invalid input')
            continue

print('Number of valid inputs:', count)
print('Maximum is:', maxim)
print('Minimum is:', minim)