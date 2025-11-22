from math import lcm 

k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())


# every kth dragon got punched 
# every lth 
# .
# .
# .
# d // k 
# d // l (which are not already covered by k)
# ... 

# 24
# 2 - 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 (12)
# 3 - 3, 6, 9, 12, 15, 18, 21, 24                 (4)
# 4 - 4, 8, 12, 16, 20, 24                        (0)
# 5 - 5, 10, 15, 20                               (1)
#                                                (17)

# nums = [False] * (d+1)
# count = 0
# for x in [k, l, m, n]:
#     for i in range(x, d+1, x):
#         if not nums[i]:
#             count += 1
#             nums[i] = True 
# print(count)

# multiples = set()
# for x in [k, l, m, n]:
#     for i in range(x, d+1, x):
#         multiples.add(i)
# print(len(multiples))

# how many common multiples between two numbers ?
# k --> d // k 
# l --> d // l 
# common --> d // lcm(k*l)

# now what if we include n ?
# k --> d // k
# l --> d // l
# n --> d // n

# k = 2 - 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 (12)
# l = 3 - 3 - 3, 6, 9, 12, 15, 18, 21, 24             (4)
# combined count of k + l = 12 + 4 = 16 
# but we counted 6, 12, 18, 24 twice, we need to remove them once
# so the combined count becomes correct. 
# the numbers which are counted twice are multiples of both 2, 3
# k ∩ l --> d // lcm(k,l)
# k ∪ l = |k| + |l| - |k ∩ l| = d//k + d//l - d//lcm(k,l)

# now, if we add "n"
# k = 2 - 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 (12)
# l = 3 - 3 - 3, 6, 9, 12, 15, 18, 21, 24             (4)
# n = 4 - 4, 8, 12, 16, 20, 24                        (0)

# k ∪ l ∪ n  = |k| + |l| + |n| 
#        (this counts values which are common k, l twice)
#        (similarily, common(l,n) and common(n,k), we need to reomve them once)
#        - (|k ∩ l| + |l ∩ n| + |k ∩ n|)
#        (this removes |k ∩ l ∩ n | thrice, which was added thrice, because of |k| + |l| + |n|)
#        but it needs to be counted once, so we add it
#        + (|k ∩ l ∩ n|)

# we see a pattern of + - + - + - 
# so for this problem, we have 4, + - + - 
# singles - doubles + tripes - quadraples 

n1 = d//k + d//l + d//m + d//n
n2 = d//lcm(k,l) + d//lcm(k,m) + d//lcm(k,n) + d//lcm(l,m) + d//lcm(l,n) + d//lcm(m,n)
n3 = d//lcm(k,l,m) + d//lcm(k,l,n) + d//lcm(k,m,n) + d//lcm(l,m,n)
n4 = d//lcm(k,l,m,n)
print(n1-n2+n3-n4)