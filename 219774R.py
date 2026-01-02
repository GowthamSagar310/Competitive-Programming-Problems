from collections import defaultdict
n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

def solve(arr1, arr2):
    m = defaultdict(int)
    for val in arr1: m[val] += 1
    for val in arr2:
        m[val] -= 1
        if m[val] < 0:
            return False
    return not any(val > 0 for val in m.values())
print("yes" if solve(arr1, arr2) else "no")