a = []
i = 2
n = 600851475143
while i <= n:
	while n % i == 0:
		n /= i
		a.append(i)
	i += 1
print max(a)
