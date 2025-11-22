from math import gcd
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    # add d to each of the sheep
    # then, need to get max(gcd)
    # gcd(x + d, y + d)

    # gcd(x, y) == gcd(x, x-y) (if x > y)
    # gcd(a1+d, a2+d) = gcd(a1+d, a1-a2)
    # gcd(a1+d, a1-a2) <= min(a1 + d, a1 - a2) 

    # upper bound on max gcd possible 
    # f(d) = min(a1-a2, min(a1+d, a2+d))
    # think in terms of graph,
    # min(a1+d, a2+d) as d increases, this increases linearly
    # and eventually crosses a1-a2
    # so after certain d, the f(d) saturates at a1-a2
    # it can never go beyond this, this is upper bound
    # for all possibel values of d
    

    maxi, mini = max(arr), min(arr)
    print(maxi - mini)
    
