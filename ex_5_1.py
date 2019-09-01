count = 0
total = 0

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
            total += num
        except:
            print('Invalid input')
            continue

print(total, count, total/count)