n, m = map(int, input().split())
arr = list(map(int, input().split()))
curr = 1
t = 0

for task in arr:
    if curr < task:
        t += task-curr
    elif curr > task:
        t += n-(curr-task)
    curr = task
print(t)

