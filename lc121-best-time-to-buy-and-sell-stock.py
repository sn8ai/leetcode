def maxProfit(nums):
	current = nums[0]
	profit = 0
	for n in nums:
		if current > n:
			current = n
		else:
			profit = max(profit, n - current)
	return profit

print(maxProfit([7,6,4,3,1]))