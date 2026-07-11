
def two_sum(nums, target):
    dict_list = {}
    for i in range(len(nums)):
        kerak = target - nums[i]
        if kerak in dict_list:        
            return [dict_list[kerak], i]
        dict_list[nums[i]] = i        
        
print(two_sum([2, 7, 11, 15],9))


