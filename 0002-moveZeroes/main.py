def moveZeroes(nums: list) -> list:
	zero_list = 0
	
	for key,value in enumerate(nums):
		if value == 0:
			zero_list +=1
			nums.pop(key)
	return nums + ([0]*zero_list)

print(moveZeroes([0,1,0,3,12]))
			
    
			
def moveZeroes(nums: list) -> list:
	zero_list = []
	
	for key,value in enumerate(nums):
		if value == 0:
			zero_list.append(0)
			nums.pop(key)
	return nums + zero_list

print(moveZeroes([0,1,0,3,12]))



def moveZeroes(nums: list) -> list:
    non_zeros = [num for num in nums if num != 0] 
    return non_zeros + [0] * (len(nums) - len(non_zeros))

print(moveZeroes([0,1,0,3,12]))