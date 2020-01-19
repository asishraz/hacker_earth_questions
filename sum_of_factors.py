Q = int(input())

while Q != 0:
	T = int(input())
	def sum_of_factors(n):
		count= 0
		half = n//2
		for i in range(1,half+1):
			if n % i == 0:
				count += i
		
		return count
	

	

	var = sum_of_factors(T)
	print(var)
	
	Q -= 1
