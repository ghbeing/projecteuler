def ispalindrome(s):
	if not s or len(s) == 1:
		return True
	return s[0] == s[-1] and ispalindrome(s[1:-1])

def isfator(n):
	for i in range(999,99,-1):
		if n % i == 0:
			m = n/i
			if m > 99 and m < 1000:
				return True
	return False

for i in range(1000000,9999,-1):
	if ispalindrome(str(i)) and isfator(i):
		print i
		break