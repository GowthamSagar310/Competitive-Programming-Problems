from collections import defaultdict

def solve(arr):
    m = defaultdict(int)
    for val in arr:
        m[val] += 1
        if m[val] >= 3:
            return val
    return -1

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr))
