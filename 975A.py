n = int(input())
arr = input().split()
m = []
for i in range(n):
    w = arr[i]
    sw = list(sorted(set(arr[i])))
    if sw not in m:
        m.append(sw)
print(len(m))