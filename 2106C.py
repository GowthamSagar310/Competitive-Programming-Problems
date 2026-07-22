for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    known_index = -1
    min_a, max_a = a[0], a[0]
    for i in range(n):
        ai, bi = a[i], b[i]
        if bi != -1:
            known_index = i
        min_a = min(min_a, ai)
        max_a = max(max_a, ai)
    if known_index == -1:
        print(max(0, k-(max_a - min_a)+1))
    else:
        pair_total = a[known_index] + b[known_index]
        count = 1
        for ai, bi in zip(a, b):
            if bi == -1:
                replace = pair_total-ai
                if replace > k or replace < 0:
                    count = 0
                    break
            elif ai + bi != pair_total:
                count = 0
                break
        print(count)
