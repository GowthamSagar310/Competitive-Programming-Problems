n = int(input())
arr = list(map(int, input().split()))
maxi = 1
count = 1
for i in range(1, n):
    if arr[i] >= arr[i-1]:
        count += 1
    else:
        count = 1
    maxi = max(maxi, count)
print(maxi)