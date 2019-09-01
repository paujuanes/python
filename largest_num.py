num1 = int(input('Type the first number:\n'))
num2 = int(input('Type the second number:\n'))
num3 = int(input('Type the third number:\n'))

if num1 >= num2 and num1 >= num3:
    print (num1, 'is the largest number.')

elif num2 >= num1 and num2 >= num3:
    print (num2, 'is the largest number.')

else:
    print (num3, 'is the largest number.')