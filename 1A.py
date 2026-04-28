from math import ceil
n, m, a = map(int, input().split())


"""
1. sqaure has to be completely covered. 
2. covered square area can be larged than n x m, that is tiles can go outside
3. what is the least number of squares ? 


fill the rows first. 
number of tiles to fill one complete row = ceil(n/a)
ceil(max(m-a, 0)/a)
"""

# print(max(ceil(m/a),1) * max(ceil(n/a), 1))
print(ceil(m/a) * ceil(n/a)) # since n,m,a are >= 1 ceil(m/a) cannot be zero, it will always be 1 if m < a, so no need of max()