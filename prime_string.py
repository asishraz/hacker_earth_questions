import math
T = int(input())
while T != 0:
    st = input()
    dict = {}
    for i in st:
        if i not in dict:
            dict.update({i:st.count(i)})
    
    length = len(dict)
    square = round(math.sqrt(length))
    #print(length,square,end=' ')
    #print
    for i in range(2,square+1):
        if length % i == 0:
            print('No')
    else:
        print('Yes')
        break

    T -= 1
    
