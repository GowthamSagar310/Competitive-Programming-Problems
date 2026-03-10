n = int(input())
arr = list(map(int, input().split()))
"""
0 1 ... n-2
p2, p3, ..... pn

"""
res = [n]
before = n
while before != 1:
    before = arr[before-2]
    res.append(before)

print(*reversed(res))