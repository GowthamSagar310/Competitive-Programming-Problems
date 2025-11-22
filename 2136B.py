for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())

    # 00101011
    # 56172834
    
    # 11011
    # 12534

    # if there k consecutive 1s, it is never possible
    res = [-1] * n
    mini, maxi = 1, n
    is_possible = True
    c = 0
    for i,l in enumerate(s):
        if l == '0':
            res[i] = maxi
            maxi -= 1
            c = 0
        else:
            c += 1
            if c >= k:
                is_possible = False
                break
            res[i] = mini
            mini += 1

    if is_possible:
        print("YES")
        print(*res)
    else:
        print("NO")
