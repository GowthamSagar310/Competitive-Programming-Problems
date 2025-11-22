for _ in range(int(input())):
    n, H, M = map(int, input().split())
    time = H * 60 + M
    mini = float("inf")
    for _ in range(n):
        h, m = map(int, input().split())
        current_time = h * 60 + m
        difference = current_time - time
        if difference < 0:
            difference += 24 * 60
        mini = min(mini, difference)
    print(mini // 60, mini % 60)