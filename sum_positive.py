sum = 0
i = 1

while True:
    n = float(input('Enter a number to add:\n>>>'))
    if i == 5:
        print('[To stop adding, enter a negative number ;)]')
    
    if n<0:
        print('Sorry, only positive numbers.\nThe sum is: ', sum)
        break
    sum += n
    i += 1