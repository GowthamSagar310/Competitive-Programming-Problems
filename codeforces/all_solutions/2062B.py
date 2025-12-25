for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    # for each clock, can we just check if we can comeback in time ?
    # a1 a2 a3 a4 a5
    # how many steps does it take for a1 (n - 0) * 2, (0 + 0) * 2
    # how many steps does it take for a2 (n - 1) * 2, (0 + 1) * 2

    for i in range(n):
        left, right = (i) * 2, abs(n-1-i) * 2
        if arr[i] <= max(left, right):
            print("NO")
            break
    else:
        print("YES")

