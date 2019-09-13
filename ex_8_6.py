'''
Exercise 8.6

*Solution by Pau Juanes, Sep 13th 2019*
'''

lst = list()

while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    
    try:
        int_num = int(num)
    except:
        print('Invalid input')
        quit()
        
    lst.append(num)

print(lst)
print('Maximum: ', max(lst))
print('Minimum: ', min(lst))