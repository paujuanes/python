def max_end3(nums):
    mx = max(nums)
    for i in range(len(nums)):
        nums[i] = mx
    return nums

print(max_end3([1, 2, 3]))
print(max_end3([1, 11, 3]))
print(max_end3([13, 2, 3]))
print(max_end3([1, 21, 3]))