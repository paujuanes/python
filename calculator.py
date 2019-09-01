print('Welcome to this simple and humble calculator.')
int1 = float(input('Enter the first number: '))
int2 = float(input('Enter the second number: '))
operator = str(input('Select an operation: + - * /  '))
if operator == '+':
    result = int1 + int2
    print('The result is: ', result)
elif operator == '-':
    result = int1 - int2
    print('The result is: ', result)
elif operator == '*':
    result = int1 * int2
    print('The result is: ', result)
elif operator == '/':
    result = int1 / int2
    print('The result is: ', result)
else:
    print('The operator ', operator, ' is not valid.')