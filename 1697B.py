n, q = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

pre = [arr[0]]
for i in range(1, n):
    pre.append(pre[-1] + arr[i])

for _ in range(q):
    x, y = map(int, input().split())
    left_index = n-x
    right_index = n-x+y-1
    free_items = pre[right_index]-(pre[left_index-1] if left_index > 0 else 0)
    print(free_items)