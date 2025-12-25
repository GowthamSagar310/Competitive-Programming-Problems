n, s = map(int, input().split())
arr = list(map(int, input().split()))

# n mugs 
# but only n-1 friends
# there are two mugs with > s volume, NO

print("YES" if sum(arr)-max(arr) <= s else "NO")