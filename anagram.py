t = int(input())
count = 0
while t != 0:
    a = 'tttttttttttttttttttttttttttttttttttttsssssssssssssssss'
    b = 'sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss'
    #a = sorted(a)
    #b = sorted(b)
    #a =list(dict.fromkeys(a)) 
    #b = list(dict.fromkeys(b))
    
    for i in a:
        if i not in b:
            count += 1
    for j in b:
        if j not in a:
            count += 1
    print(count)
    
    t -= 1
    
    
