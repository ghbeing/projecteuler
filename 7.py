def isprime(x,li):
	for prime in li:
		if prime*prime > x:
			break
		elif x % prime == 0:
			return False
	return True


a = [3,5]
m = 7
n = 7
i = 3

while True:
	if i == 10001:
		break
	if isprime(m,a):
		a.append(m)
		i += 1
		n = m
	m += 2

print n