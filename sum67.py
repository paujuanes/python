
def sum67(nums):
    need_sum = True
    six = False
    sum = 0
    for i in nums:
        if i == 6:
            need_sum = False
            six = True
        elif i == 7:
            need_sum = True
            if not six:
                sum += i
            six = False
        elif need_sum:
            sum += i
    return sum
'''
def sum67(nums):
    if len(nums) == 0:  # If the list's empty, return 0
        return 0
    while 6 in nums:  # While there's any 6, modify the list
        for i in nums:
            if i == 6:
                start = nums.index(6)  # Find the 6
                end = nums.index(7, nums.index(6))  # Find the first 7 after the 6
                del nums[start:end+1]  # Delete the sublist between them (included)
    return sum(nums)
'''

print(sum67([7, 2, 7, 6, 2, 6, 7, 2, 7, 7, 6, 7, 6, 7]))