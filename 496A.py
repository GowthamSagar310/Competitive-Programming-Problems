n = int(input())
arr = list(map(int, input().split()))
ans = float("inf")
for j in range(1, n-1):
    maxi = -1
    for i in range(1, n):
        if i != j:
            p1 = i
            p2 = i-1 if i-1 != j else i-2
            maxi = max(maxi, arr[p1]-arr[p2])
    ans = min(ans, maxi)
print(ans)