from collections import defaultdict

def solve(arr):
    if len(arr) == 1: return [-1]

    freq = defaultdict(list)
    for i in range(n): freq[arr[i]].append(i+1)
    for k, v in freq.items(): 
        if len(v) == 1: return [-1]
    
    ans = []
    i = 0
    while i < n:
        indices = freq[arr[i]]
        shuffled = indices[1:] + [indices[0]]
        ans.extend(shuffled)
        i += len(shuffled)
    return ans

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = solve(arr)
    print(*ans)