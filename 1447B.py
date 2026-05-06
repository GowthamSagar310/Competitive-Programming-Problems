for _ in range(int(input())):
    n, m = map(int, input().split())
    s = 0
    minimum_abs_val = float("inf")
    neg_count = 0
    for _ in range(n):
        row = list(map(int, input().split()))
        for val in row:
            if val < 0:
                neg_count += 1
            minimum_abs_val = min(minimum_abs_val, abs(val))
            s += abs(val)
    
    if neg_count % 2 == 0:
        print(s)
    else:
        print(s - 2 * minimum_abs_val)
