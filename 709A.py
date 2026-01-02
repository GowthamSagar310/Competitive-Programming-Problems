n, b, d = map(int, input().split())
arr = list(map(int, input().split()))

collect_waste = 0
current_size = 0
for osize in arr:
    if osize <= b:
        current_size += osize
        if current_size > d:
            collect_waste += 1
            current_size = 0
print(collect_waste)

