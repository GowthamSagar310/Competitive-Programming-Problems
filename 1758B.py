for _ in range(int(input())):
    n = int(input())
    if n & 1:
        print(*[n] * n)
    else:
        arr = [1, 3]
        arr.extend([2] * (n-2))
        print(*arr)