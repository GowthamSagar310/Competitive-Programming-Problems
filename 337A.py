n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
mini = float("inf")
for i in range(m-n+1):
    mini = min(mini, arr[n+i-1]-arr[i])
print(mini)