for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    if n == 1:
        print("NO")
    else:
        s = abs(sum(arr))
        if s == 0 or s % 4 == 0:
            print("YES")
        else:
            print("NO")