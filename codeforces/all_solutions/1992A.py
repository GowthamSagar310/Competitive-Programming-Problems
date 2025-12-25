import heapq
import math

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    h = [a, b, c]
    heapq.heapify(h)
    for _ in range(5):
        val = heapq.heappop(h)
        heapq.heappush(h, val+1)
    print(math.prod(h))
