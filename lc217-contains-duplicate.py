def containsDuplicate(nums):
	checked = {}
	for n in nums:
		if n in checked.keys():
			return True
		else:
			checked[n] = 1
	return False