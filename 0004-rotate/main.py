nums = [1,2,3,4,5,6,7]
k = 3

# aylanish kerak degani uchun har doim aylantirdim 

def rotate(nums: list, k: int) -> list:
	for i in range(k):
		nums=[nums.pop(len(nums)-1)] + nums
	return nums


# lekin optimal yechim 

def rotate(nums: list, k: int) -> list:
    return nums[-k:] + nums[:-k]
print(rotate(nums,k))