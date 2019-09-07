def reverse3(nums):
    x = -1
    numss = list()
    for i in range(len(nums)):
        numss.append(nums[x])
        x -= 1
    return numss

print(reverse3([1, 2, 3, 4, 5, 6, 7, 8, 9]))