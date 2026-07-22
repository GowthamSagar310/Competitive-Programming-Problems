from collections import deque
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    q = deque()
    for val in arr:
        if not q:
            q.append(val)
        elif val < q[0]:
            q.appendleft(val)
        else:
            q.append(val)
    print(*q)

