n, t = map(int, input().split())
arr = list(map(int, input().split()))
curr = 1
i = 0
while i < n and curr < t:
    curr = curr + arr[i]
    i = curr-1
print("YES" if curr == t else "NO")

