from collections import Counter
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    # if v > k: (v-k)
    # if v < k: (v)
    s = 0  
    for k, v in Counter(arr).items():
        if k != v:
            s += v-k if v > k else v
    print(s)