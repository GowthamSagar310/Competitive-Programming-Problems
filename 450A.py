from math import ceil
n, m = map(int, input().split())
arr = list(map(int, input().split()))
max_steps, max_index = 0, -1
for i in range(n):
    steps = ceil(arr[i]/m)
    if steps >= max_steps:
        max_steps = steps
        max_index = i+1
print(max_index)