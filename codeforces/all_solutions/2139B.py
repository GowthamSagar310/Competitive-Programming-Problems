for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()
    current_time = m
    total_cakes = 0
    for i in range(n-1, -1, -1):
        total_cakes += current_time * arr[i]
        current_time -= 1
    print(total_cakes)
