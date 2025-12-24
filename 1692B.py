from collections import Counter

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    remove = sum(val-1 for val in Counter(arr).values())
    print(n-remove - (remove % 2))