i,j,k = 2,3,5
result = 2;
while k <= 4000000:
	result += k if k%2 == 0 else 0
	i,j = j,k
	k = i+j
print result