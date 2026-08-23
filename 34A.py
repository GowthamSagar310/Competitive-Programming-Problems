n = int(input())
arr = list(map(int, input().split()))
ans = [-1, -1]
mini = float("inf")
for i in range(n):
    j = (i + 1) % n
    if abs(arr[i]-arr[j]) < mini:
        mini = abs(arr[i]-arr[j])
        ans = [i+1, j+1]
print(*ans)