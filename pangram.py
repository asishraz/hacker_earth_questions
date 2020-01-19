st = 'i am asish'
st = st.upper()
st = st.replace(' ','')
ls = []
for i in range(0,26):
	ls.append(0)

es = []
 
for i in st:
	es.append(i)

size = len(es)



x = 0
for x in size:
	index = ord(es[x])-65
	ls[x] = 1


	
print(ls)
