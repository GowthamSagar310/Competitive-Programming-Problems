n, m = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(tuple(map(int, input().split())))
arr.sort(key=lambda x: x[1], reverse=True)

count = 0
i = 0
while i < m and n:
    boxes, matches = arr[i]
    count += matches * min(boxes, n)
    n -= min(boxes, n)
    i += 1
print(count)    