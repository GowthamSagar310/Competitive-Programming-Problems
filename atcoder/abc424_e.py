from heapq import heapify, heappop, heappush

for _ in range(int(input())):
    n, k, x = map(int, input().split())
    arr = list(map(int, input().split()))
    h = [-a for a in arr]
    heapify(h)

    val = 0
    for _ in range(k):
        val = heappop(h)
        heappush(h, val/2)
        heappush(h, val/2)

    for _ in range(x):
        val = heappop(h)

    print(-val)