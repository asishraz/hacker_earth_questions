def power_trick(x,n):
	res = 1
	while n > 0:
		if n % 2 == 0:
			res = res*x
			power_trick(x*x,n/2)
			
		elif n % 2 != 0:
			res=res*x
			power_trick(x*x,n-1)
			
		else:
			return 1
		n-=1
	print(res)

number = int(input())
power = int(input())
var = power_trick(number,power)
print(var)
