def isprime(x,li):
	for prime in li:
		if prime*prime > x:
			break
		elif x % prime == 0:
			return False
	return True


a = [2,3,5]
n = 7

while n < 2000000:
	if isprime(n,a):
		a.append(n)
	n += 2

print sum(a)