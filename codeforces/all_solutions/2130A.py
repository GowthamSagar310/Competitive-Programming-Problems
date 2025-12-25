for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(sum(a if a != 0 else 1 for a in arr))