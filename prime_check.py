import math

N = int(input())


'''
for i in range(2,square+1):
	if N % i == 0:
		print('Not a prime')
	else:
		print('Prime Number')

'''

def is_prime(n):
	square = round(math.sqrt(n))
	count = 0
	if n < 2:
		return False
	else:
		for i in range(2,square+1):
			if n % i == 0:
				return False
				count += 1
			elif n % i != 0:
				pass
		if count == 0:
			return True
		else:
			return False

		square += 1

var = is_prime(N)
print(var)	
