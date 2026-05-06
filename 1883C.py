for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    even_count = sum(1 if val % 2 == 0 else 0 for val in arr)
    mini = float("inf")
    for val in arr:
        if  val % k == 0:
            mini = 0
            break
        mini = min(mini, k-(val%k))
    print(min(mini, max(0, 2-even_count) if k == 4 else mini))