for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    # mark everything as bitwise XOR = s (ops = 1)
    # then again 
    # if n == even, everything cancels out, so 0 (ops = 2)
    # if n == odd, 
        # step 1: consider everything except 1, convert to 0 (ops = 2)
        # step 2: convert the single value into 0 (ops = 3)


    # seems like l cannot be equal to r
    if n & 1:
        print(4)
        print(1, n) # s s s s s
        print(1, n-1) # 0 0 0 0 s 
        print(n-1, n) # 0 0 0 s s
        print(n-1, n) # 0 0 0 0 0
    else:
        print(2)
        print(1, n) # s s s s 
        print(1, n) # 0 0 0 0
    
