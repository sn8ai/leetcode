def myPow(x, n):
	if (n < 0):
		return 1 / myPow(x, -n)
	elif (n == 0):
		return 1
	else:
		temp = x
		while (n != 1):
			x *= temp
			n -= 1
	return x