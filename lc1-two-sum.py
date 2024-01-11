def twoSum(nums, target):
	compliments = {}
	for i in range(len(nums)):
		if nums[i] in compliments:
			return [i, compliments[nums[i]]]
		else:
			compliments[target - nums[i]] = i