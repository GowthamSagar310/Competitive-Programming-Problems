"""
- the idea here is that, it is only possible for two lengthed subarrays
- more than two, anything other than max and min, the difference is going to change. 
"""
from math import gcd
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    for i in range(n-1):
        a, b = arr[i], arr[i+1]
        if gcd(a,b) == max(a,b)-min(a, b):
            count += 1
    print(count)