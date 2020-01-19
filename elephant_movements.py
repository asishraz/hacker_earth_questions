n = int(input())
count = 0
while n != 0:

	if n > 5:
		n = n-5
		count += 1
		continue
	elif n ==4:
		n = n -4
		count += 1
		continue
	elif n == 3:
		n = n - 3
		count += 1
		continue
	elif n ==2:
		n = n - 2
		count += 1
		continue
	elif n ==1:
		n = n - 1
		count += 1
		continue
	
	n -= 1

print(count)
