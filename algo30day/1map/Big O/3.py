def bormi(nums, target):
    s = set(nums)  
    return target in s

print(bormi([1, 2, 3], 2))