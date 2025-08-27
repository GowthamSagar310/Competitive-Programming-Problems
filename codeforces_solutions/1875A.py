def solve(a, b, n, values):
    time = 0 # total time
    current_time = b
    for i in range(n):
        time += current_time-1
        current_time = min(1 + values[i], a)
    time += current_time
    return time 

for _ in range(int(input())):
    a, b, n = map(int, input().split())
    values = list(map(int, input().split()))
    print(solve(a, b, n, values))
