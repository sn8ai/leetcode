def isPalindrome(n):
	vals = {}
	if (n < 0):
		return False
	return str(n) == str(n)[::-1]