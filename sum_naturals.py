print('Sum of n first natural numbers.')
n = int(input('Type a number: '))
sum = 0

for x in range(1, n+1):
    sum += x

print('The sum of the', n, 'first natural numbers is: ', sum)