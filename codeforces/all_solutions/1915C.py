from math import isqrt
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)

    # check if total is perfect square
    # print("YES" if isqrt(total) * isqrt(total) == total else "NO")

    # binary search solution
    l, h = 1, total
    while l <= h:
        mid = (l + h) >> 1
        square = mid * mid
        if square == total:
            l = mid
            break
        elif square < total:
            l = mid + 1
        else:
            h = mid - 1
    print("YES" if l * l == total else "NO")