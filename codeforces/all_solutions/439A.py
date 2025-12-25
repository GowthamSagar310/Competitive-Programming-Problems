n, d = map(int, input().split())
arr = list(map(int, input().split()))

total_time = sum(arr) + (n-1) * 10
if total_time > d:
    print(-1)
else:
    jokes = (n-1) * 2
    time_left = d-total_time
    jokes += (time_left) // 5
    print(jokes)