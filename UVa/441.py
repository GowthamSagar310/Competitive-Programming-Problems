# subsets of size 6 + lexicographically sorted
# 6 <= k <= 12
# maximum number of subsets = 12 choose 6 = 924 combinations
first = True
while True:
    k, *arr = map(int, input().split())
    if k == 0:
        break
    else:
        if not first:
            print()
        first = False
        for a in range(k-5):
            for b in range(a+1, k-4):
                for c in range(b+1, k-3):
                    for d in range(c+1, k-2):
                        for e in range(d+1, k-1):
                            for f in range(e+1, k):
                                print(f"{arr[a]} {arr[b]} {arr[c]} {arr[d]} {arr[e]} {arr[f]}")
