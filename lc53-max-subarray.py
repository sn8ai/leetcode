def maxSubArray(nums):
	largest = nums[0]
	current = 0

	for n in nums:
		if current < 0:
			current = 0
		current += n
		largest = max(largest, current)

	return largest