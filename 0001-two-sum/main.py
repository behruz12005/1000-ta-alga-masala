def two_sum(nums:list[int], target:int) -> list:
    if len(nums) < 2:
        return []
    for key1,value1 in enumerate(nums):
        for key2,value2 in enumerate(nums):
            if value1 + value2 == target and key1 != key2:
                return [value2 ,value1 ] if value1 > value2 else [value1,value2]
    return []



def two_sum_v1(nums:list[int], target:int) -> list:
    if len(nums) < 2:
        return []
    for key1,value1 in enumerate(nums):
        for key2 in range(key1+1,len(nums)):  # array boshida qolganlarni yigindisiga tugri kelmaydi , shuni uchun tashlab ketamiz 
            if value1 + nums[key2] == target:
                return [nums[key2] ,value1 ] if value1 > nums[key2] else [value1,nums[key2]]
            
# print(two_sum_v1([3, 5, -4, 8, 11, 1, -1, 6],10) )



def two_sum_hashmap(nums:list[int], target:int) -> list:
    hashmap = {} 
    
    for index, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:

            return [num ,complement ] if complement > num else [complement,num]

        hashmap[num] = index
    return []
print(two_sum_hashmap([5, 6, -4, 8, 11, 1, -2, 6], 10))

