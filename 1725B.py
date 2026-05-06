n, d = map(int, input().split())
arr = list(map(int, input().split()))

"""
- form teams 
- max value of a team = score of each player in the team
- should be strictly greater than d 
- player can only be used once. 
- maximum number of ways


- use bigger values to increase the values of smaller players

50 60 70 80 90 100

50, 100
60, 70, 90
"""

arr.sort()
wins = 0
l, r = 0, n-1
current = arr[r]
while l <= r:
    if current > d:
        wins += 1
        r -= 1
        current = arr[r]
    else:
        current += arr[r]
        l += 1
print(wins)