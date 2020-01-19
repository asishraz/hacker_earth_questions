S = 'All-convoYs-9-be:Alert1'
K = 4
ls =[]
for i in S:
	ls.append(i)
es =[]
for i in ls:
	es.append(ord(i)+4)

ss = []
for i in es:
	ss.append(chr(i))

z = ''.join(ss)
print(z)
