'''
Fibonacci sequence generator and checker (up to 137e60).

*Pau Juanes, Sep 13th 2019*
'''
def isFibonacci(num):
    # Generate the Fibonacci sequence first
    fibonacci = [0, 1]
    for i in range (2, 300):
        new = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(new)
    
    # print(fibonacci)
    
    # Checking if the number is in the sequence
    if num in fibonacci:
        return True
    else:
        return False

def takeNumber():
    try:
        num = int(input('Enter an integer number:\n'))
        return num
    except:
        again = input("Sorry, that's not an integer number...\nWould you like to try again?(y/n)\n")
        if again == 'y':
            takeNumber()
        else:
            print('OK, I quit.')
            quit()

num = takeNumber()

if isFibonacci(num):
    print('{} IS a Fibonacci number!'.format(num))
else:
    print('{} is NOT a Fibonacci number...'.format(num))