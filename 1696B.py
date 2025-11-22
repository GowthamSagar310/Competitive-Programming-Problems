for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    i = 0
    
    # mex(S) = smallest non-negative integer which is not present in S
    # this can be any number

    # if all zeros -> 0 ops 
    # if segment == 0 -> 1 ops 
    # if segments > 1 -> 2 ops at max

    segments = 0 # segments of non-zeros
    i = 0
    while i < n:
        if arr[i] != 0:
            segments += 1
            while i < n and arr[i] != 0:
                i += 1
        else:
            i += 1
    if segments == 0:
        print(0)
    elif segments == 1:
        # this segment obviously does not contain zero
        # so, there is only operation required because mex(this segment) = 0 
        print(1) 
    else:
        # there are multiple segments
        # which means there is 0 between them
        # choose one big segment (leftmost non-zero to rightmost non-zero)
        # replace with mex(big segment) -> we are not interested which number is the mex 
        # we know that it is some number
        # after replacement, there is only big segment, which does not have zero now. 
        # requires one more operation to replace this.
        print(2)



