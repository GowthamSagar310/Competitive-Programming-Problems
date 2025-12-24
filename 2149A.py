for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    neg_count = zero_count = 0
    mini = float("inf")
    for val in arr:
        if val < 0: 
            neg_count += 1
            mini = min(mini, val)
        if val == 0: zero_count += 1
    ops = zero_count
    if neg_count % 2 != 0:
        ops += abs(mini) + 1
    print(ops)

