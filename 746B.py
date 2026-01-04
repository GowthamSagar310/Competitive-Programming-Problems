# n = int(input())
# s = input()

# res = [""] * n
# i = (n-1) // 2 if n % 2 == 0 else n // 2

# """
# if initial n is odd, -1, +1, -2, +2, etc.
# if initial n is even, +1, -1, +2, -2 etc. from initial position
# """

# if n & 1:
#     res[i] = s[0]
#     displacement = -1
#     for j in range(1, n):
#         res[i+displacement] = s[j]
#         if displacement < 0: displacement = -displacement
#         else: displacement = -displacement - 1
# else:
#     res[i] = s[0]
#     displacement = +1
#     for j in range(1, n):
#         res[i+displacement] = s[j]
#         if displacement > 0: displacement = -displacement
#         else: displacement = -displacement + 1

# print("".join(res))

# instead of thinking at the correct indicies. 
# use a dequeue to add at the both ends 

n = int(input())
s = input()

from collections import deque
deque = deque()
for i in range(n):
    if i % 2 == 0:
        deque.append(s[i])
    else:
        deque.appendleft(s[i])

if n % 2 == 0: deque.reverse()
print("".join(deque))