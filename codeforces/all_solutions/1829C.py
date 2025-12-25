for _ in range(int(input())):
    n = int(input())
    minimum_01 = float("inf")
    minimum_10 = float("inf")
    minimum_11 = float("inf")
    for _ in range(n):
        t, s = input().split()
        if s == "01": minimum_01 = min(minimum_01, int(t))
        if s == "10": minimum_10 = min(minimum_10, int(t))
        if s == "11": minimum_11 = min(minimum_11, int(t))
    mini = min(minimum_10+minimum_01, minimum_11)
    print(mini if mini != float("inf") else -1)