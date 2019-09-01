numbers = list(range(1, 10000)) #create a list

num = int(input('What number are you looking for?\n')) 
index = 0 #variable to check length

for x in numbers:
    if index > (len(numbers)/2):
        print('Your number is not in the half list... :(')
        break
    elif x == num:
        print('Your number is in the half list! :)')
        break
    else:
        index += 1