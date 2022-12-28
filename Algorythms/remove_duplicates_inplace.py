# def removeDuplicates(nums) -> list:
# 	i = 1
# 	while i < len(nums):
# 		if nums[i] == nums[i - 1]:
# 			nums.pop(nums[i])
# 		else:
# 			i += 1
#
# 	return nums
#
#
# print(removeDuplicates([1,1,2,3,3,3,3]))


def removeDuplicates(nums):
	i = 1

	while i < len(nums):
		if nums[i] == nums[i - 1]:
			nums.pop(nums[i - 1])
			print(i, nums)
			i -=1
		else:
			i +=1

	return nums

print(removeDuplicates([1,1,2,3,3,3,3]))
