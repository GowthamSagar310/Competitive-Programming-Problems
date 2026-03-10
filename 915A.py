n, k = map(int, input().split())
arr = list(map(int, input().split()))
mini = float("inf")
for val in arr:
    if k % val == 0:
        mini = min(mini, k // val)
print(mini)