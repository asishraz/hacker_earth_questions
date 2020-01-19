s = input()
count = 1
for i in range(len(s)):
    while s[i] != s[-1]:
        if s[i] == s[i+1]:
            i +=1
        else:
            count +=1
        i+=1
 
print(count)

