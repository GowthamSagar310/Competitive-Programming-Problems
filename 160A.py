n = int(input())
arr = list(map(int, input().split()))
arr.sort()
total = sum(arr)
s = 0
i = n-1
while s <= (total // 2):
    s += arr[i]
    i -= 1
print(n-i-1)