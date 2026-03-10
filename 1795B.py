for _ in range(int(input())):
    n, k = map(int, input().split())
    min_c, max_c = 0, 0
    for _ in range(n):
        l, r = map(int, input().split())
        if l == k: min_c += 1
        if r == k: max_c += 1
    
    if min_c != 0 and max_c != 0:
        print("YES")
    else:
        print("NO")
