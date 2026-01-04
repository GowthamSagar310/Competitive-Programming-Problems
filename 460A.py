# n, m = map(int, input().split())
# total = n
# day = 1
# while total:
#     total -= 1
#     if day % m == 0:
#         total += 1
#     day += 1
# print(day)

# same problem: 
# 1. 1352C
# 2. 1296B
# 3. 460A

# think of think problem as
# 1. on every divisible day, 1 extra socks.
#    this of this as a skip day. because i used one, i gained one. so dont have to count. 
# 2. on every non-divisible day, 1 use socks and gain nothing. 
# 3. basically we are looking for 
#    nth non-divisible number by m

n, m = map(int, input().split())
print(n + (n-1)//(m-1))