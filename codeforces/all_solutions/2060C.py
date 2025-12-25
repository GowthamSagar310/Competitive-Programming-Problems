import sys
import math

def input(): return sys.stdin.readline().rstrip()

def solve(arr, n, k):

    # just see how many pairs of a+b=k are present
    # it will always be possible to choose these or less
    # 
    # 1. if alice choose some number which is not part of a+b=k, 
    #    bob has to choose, some other number which is also not part
    # 2. if alice choose some number which is part of a+b=k,
    #    bob can obviously choose the other number

    arr_s = sorted(arr)

    # count the number of pairs of a+b=k
    l, r = 0, n-1
    pairs = 0
    while l < r:
        total = arr_s[l] + arr_s[r]
        if total == k:
            pairs += 1
            l += 1
            r -= 1 
        elif total < k:
            l += 1
        else:
            r -= 1
    
    # number of numbers which are not part of pairs ? 
    # total - 2*pairs -> this is also even, because the total is even (given)
    # so, there is no case where, odd number of numbers are left out -> if yes, then 0

    print(pairs)
    

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        solve(arr, n, k)
