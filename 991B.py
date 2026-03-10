n = int(input())
arr = list(map(int, input().split()))
"""
(a1 + a2 + a3 + a4 ... an ) / n = avg
"""
arr.sort()
t = sum(arr)
i = 0
ops= 0
while (t / n) < 4.5:
    d = 5-arr[i]
    if d:
        t += d
        ops += 1
    i += 1
print(ops)