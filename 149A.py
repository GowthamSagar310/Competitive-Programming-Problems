k = int(input())
arr = list(map(int, input().split()))
arr.sort()
total = 0 
i = 11
while i >= 0 and total < k:
    total += arr[i]
    i -= 1
print(11-i if total >= k else -1)
