from math import ceil
for _ in range(int(input())):
    n, r, b = map(int, input().split())
    s = ""
    # build around "b" (< r)
    # 3 <= n <= 100
    # r > b
    # 1 <= b < r <= n
    # r + b = n
    # r = 2, b = 1 is the base case. 
    
    # b slots create b+1 spaces for r's to fill
    # k = ceil(r / (b+1))
    # atleast one of the region will be with this k
    # so the maximum number of consecutive R's will be k. 

    # distribute R equally to all the slots 
    repeat = r // (b+1)
    missed = r % (b+1)
    for i in range(b+1):
        s += "R" * (repeat + (1 if missed else 0))
        missed = max(missed-1, 0)
        if i != b:
            s += "B" 
    print(s)

