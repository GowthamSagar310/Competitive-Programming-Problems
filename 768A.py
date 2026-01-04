n = int(input())
arr = list(map(int, input().split()))
mini, maxi = min(arr), max(arr)
c1 = c2 = 0
for i in range(n):
    if arr[i] == mini: c1 += 1
    if arr[i] == maxi: c2 += 1

if mini == maxi: print(0)
else:
    print(n-c1-c2)