S = 'RrHRxcUsSrvSnTyolvsxHoGyzwBMzuLCUjcSeWmBAhodtEkgZjDkFjaXXAvjTvRfHuHGtopoxaeONzFFurfNlRdAvRYlnlfdIMsI'
#xcUsSrvSnTyolvsxHoGyzw'
low = []
upp = []

for i in S:
	if ord(i) in range(97,123):
		#low.append(chr(ord(i)-32))
		S = S.replace(i,chr(ord(i)-32))
	elif ord(i) in range(65,91):
		#upp.append(chr(ord(i)+32))
		S = S.replace(i,chr(ord(i)+32))
print(S)

'''
print(low)
print(upp)
print(low+upp)
'''



'''
rrhrXCUSSrVSNTyoLVSXhogyZwbmZULCUJCSEwmbahoDTEKgZJDKFJaXXaVJTVrFhUhgToPoXaEoNZFFUrFNLrDaVryLNLFDimSi (my o/p)
'''


''' 
rRhrXCuSsRVsNtYOLVSXhOgYZWbmZUlcuJCsEwMbaHODTeKGzJdKfJAxxaVJtVrFhUhgTOPOXAEonZffURFnLrDaVryLNLFDimSi (expected o/p)
'''
