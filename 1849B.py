"""


n monsters, 1 to n 
ai = health
k = damage

what is the order in which the monsters die ? 

"""

# from heapq import heapify, heappop, heappush
# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     h = [(-val, i) for i, val in enumerate(arr)]
#     heapify(h)
#     order = []
#     while h:
#         health, index = heappop(h)
#         health *= -1
#         health -= k
#         if health <= 0:
#             order.append(index+1)
#         else:
#             heappush(h, (-health, index))
#     print(*order)


import math
for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    # the largest gets reduced as long as it is highest
    # then we move to the next largest (which is also smallest index)
    # as this keeps on happening, 
    # there comes a stage where every health is <= k
    # then the highest health values (k) will get killed because it is takes only 1 blow. 
    # next k-1

    # hits = [(-(val % k if val % k != 0 else k), i) for i, val in enumerate(arr)]
    hits = [(-((val-1) % k), i) for i, val in enumerate(arr)]
    hits.sort()

    print(*[index+1 for _, index in hits])
