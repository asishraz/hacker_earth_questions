T = int(input())
while T != 0:
    N = int(input())
    N = int(N)
    if N % 2 == 0:
        N = N // 2
        continue
        if N == 8:
            print('YES')
    elif N % 2 != 0:
        N = 3*N + 1
        continue
    
    T -= 1
