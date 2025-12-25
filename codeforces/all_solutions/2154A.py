for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    ops = 0
    prev_one = -1
    for i in range(n):
        if s[i] == "1":
            if prev_one == -1:
                ops += 1
            else:
                # distance between current one and prev one 
                # if it is greater than k, that means there are no ones in last k-1 elements
                # so we have to protect this one. 
                if (i - prev_one + 1) > k:
                    ops += 1
            prev_one = i
    print(ops)