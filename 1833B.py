for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_i = [(val, i) for i, val in enumerate(a)]
    a_i.sort()
    b.sort()
    ans = [0] * n
    for i in range(n):
        a_val, index = a_i[i]
        b_val = b[i]
        ans[index] = b_val
    print(*ans)