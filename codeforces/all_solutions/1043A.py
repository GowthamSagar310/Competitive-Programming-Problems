# 2 2 3 2 2

# 9 < 5k-9
# 18 < 5k
# 3 < k

# 22 < 5k
# 4 < k
# 

n = int(input())
arr = list(map(int, input().split()))
k = max(max(arr), ((2 * sum(arr))) // n + 1)
print(k)

# simple ceil wont work here because, what if n exactly divides the 2 * votes ?
# we need strictly more votes, to win 
# this is ceil but adds one when it divides exactly

