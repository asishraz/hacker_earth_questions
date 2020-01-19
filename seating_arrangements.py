T = int(input())

while T != 0:
    N = int(input())
    #for window seat
    ws_list = range(1,97,12)
    ws_list_2 = range(6,102,12)
    ws_list_3 = range(12,108,12)
    ws_list_4 = range(7,103,12)
    if N in ws_list:
        print(N+11,'WS',end=' ')
        print('\r')
    elif N in ws_list_2:
        print(N+1,'WS',end=' ')
        print('\r')
    elif N in ws_list_3:
        print(N-11,'WS',end=' ')
        print('\r')
    elif N in ws_list_4:
        print(N-1,'WS',end=' ')
        print('\r')
        
    #for middle seat
    ms_seat = range(2,98,12)
    ms_seat1 = range(5,101,12)
    ms_seat2 = range(11,107,12)
    ms_seat3 = range(8,104,12)
    if N in ms_seat:
        print(N+9,'MS',end=' ')
        print('\r')
    elif N in ms_seat1:
        print(N+3,'MS',end=' ')
        print('\r')
    elif N in ms_seat2:
        print(N-9,'MS',end=' ')
        print('\r')
    elif N in ms_seat3:
        print(N-3,'MS',end=' ')
        print('\r')
        
    #for aisle seat
    as_seat = range(3,99,12)
    as_seat2 = range(4,100,12)
    as_seat3 = range(10,106,12)
    as_seat4 = range(9,105,12)
    if N in as_seat:
        print(N+7,'AS',end=' ')
        print('\r')
    elif N in as_seat2:
        print(N+5,'AS',end=' ')
        print('\r')
    elif N in as_seat3:
        print(N-7,'AS',end=' ')
        print('\r')
    elif N in as_seat4:
        print(N-5,'AS',end=' ')
        print('\r')
    
    
    T -=1
