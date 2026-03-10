n, k = map(int, input().split())
arr = list(map(int, input().split()))

allot = [[] for _ in range((n*k)+1)]
for i, val in enumerate(arr, 1): allot[i].append(val)

def is_present(allot, target):
    for val in allot:
        for value in val:
            if value == target:
                return True
    return False

for i in range(1, (n*k)+1):
    v = 1
    while v <= (n*k) and len(allot[i]) < n:
        if not is_present(allot, v):
            allot[i].append(v)
        v += 1
    print(" ".join(map(str, allot[i])))