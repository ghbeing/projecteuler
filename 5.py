def gcd(a,b):
	return b if a % b == 0 else gcd(b,a%b)

def lcm(a,b):
	return a * b / gcd(a,b)

n = 1
for i in range(1,21):
	n = lcm(i,n)
print n
