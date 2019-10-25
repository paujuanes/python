def is_armstrong_number(number):
    strNum = str(number)
    digitSum = 0
    for i in range(len(strNum)):
        digit = int(strNum[i])**len(strNum)
        digitSum += digit
    if number == digitSum: return True
    return False

for i in range(10000000):
    if is_armstrong_number(i):
        print(i)