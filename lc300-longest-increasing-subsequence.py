def longestIncreasingSubsequence(numbers):
	n = len(numbers)
	dp = [1] * n
	for i in range(n):
		for j in range(i):
			if ( numbers[j] < numbers[i] and dp[i] < 1 + dp[j] ):
				dp[i] = dp[j] + 1
	return max(dp)