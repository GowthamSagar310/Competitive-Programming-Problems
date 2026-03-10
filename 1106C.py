n = int(input())
arr = list(map(int, input().split()))
arr.sort()
s = 0
l, r = 0, n-1
while l < r:
    s += (arr[l] + arr[r]) ** 2
    l += 1 
    r -= 1
print(s)