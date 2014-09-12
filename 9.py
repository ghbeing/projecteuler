import math

def product(n):
	for a in range(1,n+1):
		for b in range(1,n-a+1):
			c = n-a-b
			if a*a + b*b == c*c:
				return a*b*c

print product(1000)