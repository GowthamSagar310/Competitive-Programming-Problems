for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    # 0 val 0 val 0 -> mex will be 0
    # if there are more zeros than values, then mex will be != 0
    
    # 0 0 0 0 -> z_count = 4 rem = 0 -> 1 
    # 1 1 1 1 -> z_count = 0 rem = 4 -> 0
    # 0 0 1 1 
    # 0 1 0 0

    # ans is always <= 2
    # if there only zeroes - 1 
    # if there no zeroes - 0
    # if there are more zeroes than numbers, more than ceil of half
    #       - the best we need to aim for is MEX 1, we need to avoid the sum 1 for that
    #       - how can we avoid sum 1 ? 
    #       - sum 1 is only possible when there only 1 and 0, because they have to meet somewhere
    #       - if there is atleast on val >= 2, then we can put that at the boundary of 0 and val [0, val, 1]
    #       - so sum 1 is always avoided and 1 will be mex


    z_count = arr.count(0)
    rem = n - z_count 
    total = sum(arr)

    if z_count == 0:
        print(0)
    elif z_count == n:
        print(1)
    elif z_count - rem <= 1:
        print(0)
    else:
        print(1 if max(arr) != 1 else 2)
