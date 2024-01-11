def validAnagram(s, t):
	chars = {}
	for i in range(len(s)):
		if s[i] not in chars.keys():
			chars[s[i]] = 1
		else:
			chars[s[i]] += 1
	for j in range(len(t)):
		if t[j] not in chars.keys():
			return False
		else:
			chars[t[j]] -= 1
	return True